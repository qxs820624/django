#coding=utf-8
from django.db import models
from django.utils import timezone
from datetime import datetime, date
# Create your models here.
'''
参考 http://www.dannysite.com/blog/7/
'''
from django.contrib import admin

# 标签
class Tag(models.Model):
	tag_name = models.CharField(verbose_name = '标签', max_length=20)
	create_time = models.DateTimeField( verbose_name = '创建时间', auto_now_add=True)

	def __unicode__(self):
		return u'%s' % (self.tag_name)
	def __str__(self):
		return u'%s' % (self.tag_name)
	class Meta:
		verbose_name = "标签"
		verbose_name_plural = "标签"

# 作者
class Author(models.Model):
	nickname = models.CharField( verbose_name = '昵称', max_length=20)
	work = models.CharField( verbose_name = '工作', max_length=20)
	company = models.CharField( verbose_name = '单位', max_length=50)
	email = models.CharField( verbose_name = '邮箱', max_length=20)

	def __unicode__(self):
		return u'%s' % (self.nickname)
	def __str__(self):
		return u'%s' % (self.nickname)
	
	class Meta:
		verbose_name = "作者"
		verbose_name_plural = "作者"
	
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('nickname', 'email', 'company')
	search_fields = ('nickname',)
# 分类
class Classification(models.Model):
	name = models.CharField( verbose_name = '类别', max_length=20, default = '随笔')

	def __unicode__(self):
		return u'%s' % self.name
	def __str__(self):
		return u'%s' % self.name
	
	class Meta:
		verbose_name = "分类"
		verbose_name_plural = "分类"

# 文章
class Blogs(models.Model):
	TYPE_CHOICES  = {
	        ('Txt','文本'),
	        ('Blend','图文'),
	        ('Photo','图片'),
	        ('Link','链接'),
	}
	title = models.CharField( verbose_name = '标题', max_length = 150)
	subTitle = models.CharField(verbose_name = '子标题', max_length=50, blank=True)
	body = models.TextField(verbose_name = '内容')
	publish_time = models.DateTimeField(verbose_name = '发布时间', auto_now_add=True)
	update_time = models.DateTimeField(verbose_name = '更新时间', default = timezone.now())
	classification = models.ForeignKey(Classification, verbose_name = '分类', null = True)
	tags = models.ManyToManyField(Tag, verbose_name = '标签', blank=True)
	blog_type = models.CharField(verbose_name = '正文类型', max_length=50, default='Txt',choices = TYPE_CHOICES)
	blog_imgurl = models.CharField(verbose_name = '头像地址', max_length=50, blank=True, null=True)
	blog_author = models.ForeignKey(Author, verbose_name= '作者')
	blog_ismarkdown = models.BooleanField(verbose_name = '是否MD格式', default=False)
	blog_like = models.IntegerField( verbose_name = '喜欢数', null=True)
	blog_clicknum = models.IntegerField(verbose_name = '点击数', null=True)
	
	def __unicode__(self):
		return u'%s' % self.title
	def __str__(self):
		return u'%s' % self.title
	
	class Meta:
		verbose_name = "文章"
		verbose_name_plural = "博客"
		#db_table="data"  
		#app_label='UserDBs'
	

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'subTitle', 'classification', 'blog_author', 'publish_time', 'update_time') #替预览
	list_filter = ('publish_time',)
	exclude=[]#不包括
	#inlines=[Author]#类表出来，注意text类有f k
	#search_fields= ['title', 'classification', 'blog_author'] #搜索菜单
	search_fields= ('title', ) #搜索菜单
	date_hierarchy = 'publish_time'
	ordering = ('-publish_time',)
	#使用filter_horizontal，(支持拖拽),filter_vertical可以从现有的选项中多选。一个为横排，一个为竖排。
	filter_horizontal = ('tags',)
	fieldsets=[
		('必填',{'fields':['title','classification','blog_author', 'publish_time']}),  
		('选填',{'fields':['subTitle','algupdate_timeo']})  
	]	

admin.site.register(Blogs,BlogPostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Classification)
admin.site.register(Tag)
