from django.db import models
from django.contrib import admin
from draceditor.widgets import AdminDraceditorWidget

from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	formfield_overrides = {
            models.TextField: {'widget': AdminDraceditorWidget},
    }

admin.site.register(Post, PostAdmin)
