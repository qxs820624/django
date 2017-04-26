from django.contrib import admin

# Register your models here.
from . import models

class RoleAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'gender')
	search_fields = ('name', 'gender')

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'gender')
	search_fields = ('name', 'gender')

class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'argument_list','describe')  
    search_fields = ('name', 'url')

admin.site.register(models.Role,RoleAdmin)
admin.site.register(models.Employee,EmployeeAdmin)
admin.site.register(models.Permission)