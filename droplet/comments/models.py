from django.db import models

# Create your models here.
from draceditor.models import DraceditorField

class Post(models.Model):
	description = DraceditorField()
