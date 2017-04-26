from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field

from .models import Package


class OrderForm(forms.ModelForm):
    """order form"""
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            Field('memory'),
            Field('plan_id'),
            Submit('order', 'Order Now',css_class="btn btn-primary"),
            )

    class Meta:
        model = Package
        fields = ['memory','plan_id']
