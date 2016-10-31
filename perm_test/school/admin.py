# coding=utf-8
from django.contrib import admin

# Register your models here.
from . import models

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sex')   #添加字段显示
    search_fields = ('name', 'sex')         #添加快速查询栏
    list_filter=('sex',)                    #添加过滤（这里是过滤性别）
    ordering=('name',)                      # 排序（这里以姓名排序，加‘-’表示降序）
    fields = ('age', 'sex',)                #排除一些不想被其他人编辑的fields（不包含在内的不能编辑，这里name不能编辑了）
    # filter_horizontal = ('authors',)      #从‘多选框’的形式改变为‘过滤器’的方式，水平排列过滤器，must be a ManyToManyField，且不能用于 ForeignKey字段，默认地，管理工具使用`` 下拉框`` 来展现`` 外键`` 字段
    # filter_vertical = ('authors',)        #同上，垂直排列过滤器
    # raw_id_fields = ('publisher',)        #将ForeignKey字段从‘下拉框’改变为‘文本框’显示



class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'argument_list','describe')   #添加字段显示
    search_fields = ('name', 'url')   #添加快速查询栏


admin.site.register(models.Student,StudentAdmin)
admin.site.register(models.Permission,PermissionAdmin)
