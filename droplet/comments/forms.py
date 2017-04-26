# coding=utf-8

#from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from applications.models import Review
from draceditor.fields import DraceditorFormField

class CommentForm(ModelForm):
	"""My Customized Comment Form.

	Just add some features via crispy.
	"""
	description = DraceditorFormField()
	class Meta:
                model = Review
                fields = ('rating', 'reviews')
		
