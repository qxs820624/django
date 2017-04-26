from django.contrib import admin
from .models import Plan,CloudConsole,Package,Server

admin.site.register(Plan)
admin.site.register(CloudConsole)

class PackageAdmin(admin.ModelAdmin):
   list_display = ('name','status','created_date','created_by','updated_date','updated_by')
   ordering = ('-created_date', )
   list_filter = ('name', )

admin.site.register(Package,PackageAdmin)

admin.site.register(Server)

