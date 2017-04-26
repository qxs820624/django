from __future__ import unicode_literals
from datetime import datetime
from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Permission(models.Model):
    name = models.CharField("permType", max_length=64)
    url = models.CharField('URLName', max_length=255)
    chioces = ((1, 'GET'), (2, 'POST'))
    # per_method = models.SmallIntegerField('method', choices=chioces, default=1)
    create_date = models.DateTimeField(u'createTime', default=datetime.now, editable = True)
    update_time = models.DateTimeField(u'updateTime', default=datetime.now, null=True)

    argument_list = models.CharField('paraList', max_length=255, help_text='multiple arguments split by comma', blank=True, null=True)
    describe = models.CharField('description', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Permission'
        verbose_name_plural = verbose_name
        
        permissions = (
            ('views_student_list', 'get information'),
            ('views_student_info', 'get detail'),
        )


class Role(models.Model):
    name = models.CharField('name', max_length=64)
    age = models.SmallIntegerField('age')
    choices = (
        (1, 'male'),
        (2, 'female'),
        (3, 'uncertain')
    )
    gender = models.SmallIntegerField('gender', choices=choices)


    perms = models.ManyToManyField(Permission)
    permlist = []

    def save(self, *args, **kwargs):
        super(Role, self).save()
        for i in self.permlist:
            p, created = Permission.objects.get_or_create(name=i)
            self.perms.add(p)


    
    def __str__(self):
        return self.name

    def __unicode__(self):
        #return u'%s %d %s' % (self.name, self.age, self.gender)
        return u'%s' % self.name

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = verbose_name



class Employee(models.Model):
    name = models.CharField('name', max_length=64)
    age = models.SmallIntegerField('age')
    choices = (
        (1, 'male'),
        (2, 'female'),
        (3, 'uncertain')
    )
    gender = models.SmallIntegerField('gender', choices=choices)
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        #return u'%s %d %s' % (self.name, self.age, self.gender)
        return u'%s' % self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = verbose_name