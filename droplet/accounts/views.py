from __future__ import unicode_literals
import random
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from django.contrib.auth import get_user_model,logout
from django.contrib import auth
from django.contrib import messages
from authtools import views as authviews
from braces import views as bracesviews
from django.conf import settings
from . import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http.response import HttpResponseRedirect
User = get_user_model()
import logging
logger = logging.getLogger("project")

from .send_mail.send_mail import send_signup_mail
from .utils import (decode,InvalidCode,get_confirmation_url)


class LoginView(bracesviews.AnonymousRequiredMixin,
                authviews.LoginView):
    template_name = "accounts/login.html"
    form_class = forms.LoginForm

    def form_valid(self, form):
        redirect = super(LoginView, self).form_valid(form)
        remember_me = form.cleaned_data.get('remember_me')
        if remember_me is True:
            ONE_MONTH = 30*24*60*60
            expiry = getattr(settings, "KEEP_LOGGED_DURATION", ONE_MONTH)
            self.request.session.set_expiry(expiry)
        return redirect

class LogoutView(authviews.LogoutView):
    url = reverse_lazy('home')


class SignUpView(bracesviews.AnonymousRequiredMixin,
                 bracesviews.FormValidMessageMixin,
                 generic.CreateView):
    form_class = forms.SignupForm
    model = User
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('home')
    form_valid_message = """Thanks! Next, click the confirmation link that was just emailed to you.
                         If you don't see our email within a few minutes, please check your Spam
                         folder."""

    def form_valid(self, form):
        host_name = self.request.META.get('HTTP_HOST',None)
        r = super(SignUpView, self).form_valid(form)
        email = form.cleaned_data["email"]
        name = form.cleaned_data["name"]
        absolute_url = get_confirmation_url(email,self.request,name)
        try:
            query_name = User.objects.get(name=name)
            query_name.is_active = False
            query_name.save()
            logger.info('a new inactive user {} created'.format(query_name))
        except:
            pass
        #send email
        to = email
        send_signup_mail(name,absolute_url,to)
        return r


def confirmation_view(request, code):
    """email confirm"""
    try:
        email,username = decode(code)
    except InvalidCode as e:
        messages.warning(request,"{}".format(e))
        return redirect('/')
    try:
        user = User.objects.get(name = username)
    except ObjectDoesNotExist as e:
        messages.warning(request,"{}".format(e))
        return redirect('/')
    if user.is_active:
        messages.warning(request,"Your accouts has already actived!,you can login now" )
        return HttpResponseRedirect(reverse_lazy('home'))
    user.is_active = True
    user.save()
    messages.success(request,"Your accouts is active,you can login now" )
    return HttpResponseRedirect(reverse_lazy('home'))


class PasswordChangeView(authviews.PasswordChangeView):
    form_class = forms.PasswordChangeForm
    template_name = 'accounts/password-change.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        logout(self.request)
        messages.success(self.request,
                         "Your password was changed, "
                         "hence you have been logged out. Please relogin")
        return super(PasswordChangeView, self).form_valid(form)


class PasswordResetView(authviews.PasswordResetView):
    form_class = forms.PasswordResetForm
    template_name = 'accounts/password-reset.html'
    success_url = reverse_lazy('accounts:password-reset-done')
    subject_template_name = 'accounts/emails/password-reset-subject.txt'
    email_template_name = 'accounts/emails/password-reset-email.html'


class PasswordResetDoneView(authviews.PasswordResetDoneView):
    template_name = 'accounts/password-reset-done.html'


class PasswordResetConfirmView(authviews.PasswordResetConfirmAndLoginView):
    template_name = 'accounts/password-reset-confirm.html'
    form_class = forms.SetPasswordForm


class OrderManage(generic.TemplateView):
    """accounts panel"""
    template_name = 'accounts/ordermanage.html'
    http_method_names = ['get']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(OrderManage,self).dispatch(request,*args, **kwargs)

    def get(self, request, *args, **kwargs):
        user = self.request.user
        kwargs["user"] = user
        return super(OrderManage, self).get(request, *args, **kwargs)



