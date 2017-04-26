# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField('姓名', max_length=64)
    age = models.SmallIntegerField('年龄')
    choices = (
        (1, '男'),
        (2, '女'),
        (3, '未知')
    )
    sex = models.SmallIntegerField('性别', choices=choices)
    
    def __str__(self):
        #return '%s %d %s' % (self.name, self.age, self.sex)
        return self.name

    def __unicode__(self):
        #return u'%s %d %s' % (self.name, self.age, self.sex)
        return u'%s' % self.name

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = verbose_name

class Permission(models.Model):
    name = models.CharField("权限名称", max_length=64)
    url = models.CharField('URL名称', max_length=255)
    chioces = ((1, 'GET'), (2, 'POST'))
    per_method = models.SmallIntegerField('请求方法', choices=chioces, default=1)
    argument_list = models.CharField('参数列表', max_length=255, help_text='多个参数之间用英文半角逗号隔开', blank=True, null=True)
    describe = models.CharField('描述', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = verbose_name
        #权限信息，这里定义的权限的名字，后面是描述信息，描述信息是在django admin中显示权限用的
        permissions = (
            ('views_student_list', '查看学员信息表'),
            ('views_student_info', '查看学员详细信息'),
        )


class TagManager(models.Manager):
    def get_or_create(self, **kwargs):
        defaults = kwargs.pop('defaults', {})
        articalslist = defaults.pop('articalslist', {})
        Tag.articalslistlist = articalslist
        kwargs.update(defaults)
        super(TagManager, self).get_or_create(**kwargs)

class Tag(models.Model):
    name = models.CharField(u"标签名", max_length=30)
    articals = models.ManyToManyField(Entry)
    articalslist = []
    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return u'%s' % self.name
    
    def save(self, *args, **kwargs):
        super(Tag, self).save()
        for i in self.articalslist:
            p, created = Entry.objects.get_or_create(name=i)
            self.articals.add(p) 
        self.articalslist = []

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
    
class EntryManager(models.Manager):
    def get_or_create(self, **kwargs):
        defaults = kwargs.pop('defaults', {})
        taglist = defaults.pop('taglist', {})
        Entry.taglist = taglist
        kwargs.update(defaults)
        super(EntryManager, self).get_or_create(**kwargs)

class Entry(models.Model):
    title = models.CharField("标题", max_length=100)
    pub_date = models.DateField("发布日期", blank=True, null=True)
    content = models.TextField("正文")
    tags = models.ManyToManyField(Tag)
    taglist = []
    objects = EntryManager()
    
    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return u'%s' % self.title
    
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    
    def save(self, *args, **kwargs):
        super(Entry, self).save()
        for i in self.taglist:
            p, created = Tag.objects.get_or_create(name=i)
            self.tags.add(p) 
        self.taglist = []

