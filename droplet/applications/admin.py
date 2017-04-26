from django.contrib import admin
from .models import \
   (Product,ScreenShot,ProductCategories,
    ProductToCategory,ProgramLanguage,Platform,Database,
    Review,ProductVideo)

class ProductAdmin(admin.ModelAdmin):
   search_fields = ('type', 'name','vendor_name','created_date')
   #fields = ('type', 'name','platform','language','database')
   list_display = ('name', 'type','vendor_name','free_plan','status','created_date','created_by','updated_date','updated_by')
   ordering = ('-created_date', )
   #raw_id_fields = ('language','platform','database')
   list_filter = ('name', )

admin.site.register(Product,ProductAdmin)

class ScreenShotAdmin(admin.ModelAdmin):
   list_display = ('product_id', 'software_version','title','url','created_date','created_by','updated_date','updated_by')
   search_fields = ('product_id', 'software_version','title','url','created_date','created_by','updated_date','updated_by')
   ordering = ('id',)
   list_filter = ('product_id', 'software_version','title','url','created_date','created_by','updated_date','updated_by')

admin.site.register(ScreenShot,ScreenShotAdmin)

class ProductCategoriesAdmin(admin.ModelAdmin):
   list_display = ('name', 'description','feature01','feature02','feature03','feature04','status','created_date','created_by')
   search_fields = ('category_name', 'status','created_date','created_by')
   ordering = ('-created_date', )
   list_filter = ('name', 'status','created_date','created_by')

admin.site.register(ProductCategories,ProductCategoriesAdmin)

class ProductToCategoryAdmin(admin.ModelAdmin):
   list_display = ('product_id', 'category_id')
   search_fields = ('product_id', 'category_id')
   ordering = ('product_id', )
   list_filter = ('product_id', 'category_id')

admin.site.register(ProductToCategory,ProductToCategoryAdmin)

admin.site.register(ProgramLanguage)
admin.site.register(Platform)
admin.site.register(Database)
admin.site.register(Review)
admin.site.register(ProductVideo)


