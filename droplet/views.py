from django.views import generic
from django.shortcuts import render
from applications.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
import logging
logger = logging.getLogger("project")


# class HomePage(generic.TemplateView):
#     model = Product
#     template_name = "home.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(HomePage, self).get_context_data( **kwargs)
#         redis = Product.objects.get(name='Redis')
#         context = {}
#         if redis:
#             context['summary'] = redis.summary
#         return context


#redefine the home view
def home(request):
    user = request.user
    query_product = Product.objects.all()
    logger.info('find products {} '.format(list(query_product)))
    group = get_user_group(request)
    return render(request,"new_home.html",{'group':group,'product_list':query_product})


class AboutPage(generic.TemplateView):
    template_name = "new_about.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['group'] = get_user_group(request)
        return self.render_to_response(context)


class SupportPage(generic.TemplateView):
    template_name = "support.html"


class NetworkPage(generic.TemplateView):
    template_name = "new_network.html"

    def get_context_data(self,**kwargs):
        context = super(NetworkPage,self).get_context_data(**kwargs)
        context['group'] = get_user_group(self.request)
        return context



class Price(generic.TemplateView):
    template_name = "new_price.html"

    def get(self,request,*args,**kwargs):
        context = self.get_context_data(**kwargs)
        context['group'] = get_user_group(request)
        return self.render_to_response(context)


def get_user_group(request):
    """get user group"""
    user = request.user
    group = None
    if not isinstance(user,AnonymousUser):
        try:
            group = user.groups.all()[0]
        except:
            group = None
    return group
