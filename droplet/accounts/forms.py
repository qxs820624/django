from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model,password_validation
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator,validate_password

User = get_user_model()


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        self.fields["username"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field('username', placeholder="Enter Email", autofocus=""),
            Field('password', placeholder="Enter Password",),
            Field('remember_me',css_class='text-center '),
            Submit('sign_in', 'Log in',
                   css_class="btn btn-primary"),
            )


class SignupForm(authtoolsforms.UserCreationForm):

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
        'duplicate_username': _("A user with that %(username)s already exists."),
        'duplicate_name': _("A user with that %(name)s already exists."),
        'short_name': _("The username %(name)s is too short."),
    }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        #self.helper.form_show_errors = False
        self.fields["email"].widget.input_type = "email"

        self.helper.layout = Layout(
            Field('email', placeholder="Enter Email",css_class="form-control ", autofocus=""),
            Field('name', placeholder="Enter Full Name",css_class="form-control "),
            Field('password1', placeholder="Enter Password",css_class="form-control "),
            Field('password2', placeholder="Re-enter Password",css_class="form-control "),
            Submit('sign_up', 'Sign up', css_class="btn-warning"),
            )

    def clean_password1(self):
        # check the password
        password = self.cleaned_data.get("password1")
        validate_password(password)
        return password

    def clean_name(self):
        # Check the name
        name = self.cleaned_data.get("name")
        if len(name) < 2:
            raise forms.ValidationError(self.error_messages['short_name'] % {
                'name': name,
            })
        try:
            User.objects.get(name=name)
            raise forms.ValidationError(self.error_messages['duplicate_name'] % {
                'name': name,
            })
        except User.DoesNotExist:
            return name
        return name

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(self.error_messages['password_mismatch'])
        return password2

class PasswordChangeForm(authforms.PasswordChangeForm):

    new_password1 = forms.CharField(label=_("New password"),
                                    widget=forms.PasswordInput,)
    new_password2 = forms.CharField(label=_("Confirm password"),
                                    widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'

        self.helper.layout = Layout(
            Field('old_password', placeholder="Enter old password",css_class="form-control",
                  autofocus=""),
            Field('new_password1', placeholder="Enter new password",css_class="form-control",),
            Field('new_password2', placeholder="Enter new password (again)",css_class="form-control",),
            Submit('pass_change', 'Change Password', css_class="btn-warning",),
            )


class PasswordResetForm(authtoolsforms.FriendlyPasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'

        self.helper.layout = Layout(
            Field('email', placeholder="Enter email",
                  autofocus=""),
            Submit('pass_reset', 'Reset Password', css_class="btn-warning"),
            )


class SetPasswordForm(authforms.SetPasswordForm):
    """change new_password"""
    new_password1 = forms.CharField(label=_("New password"),
                                    widget=forms.PasswordInput,)
    new_password2 = forms.CharField(label=_("Confirm password"),
                                    widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'

        self.helper.layout = Layout(
            Field('new_password1', placeholder="Enter new password",
                  autofocus=""),
            Field('new_password2', placeholder="Enter new password (again)"),
            Submit('pass_change', 'Change Password', css_class="btn-warning"),
            )