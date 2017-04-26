from django.db import models
from django.conf import settings


class OpenstackAccount(models.Model):
    """openstack user id"""
    user=models.ForeignKey(settings.AUTH_USER_MODEL)
    employeeId = models.CharField('EmployeeId',max_length= 10, null = False, default = "00000000")
    username=models.CharField('Name',max_length=256)
    password=models.CharField('Password',max_length=256,default='123456')
    created_date = models.DateTimeField('CreatedDate',auto_now_add = True)
    created_by = models.CharField('CreatedBy',max_length=256,null=True, blank=True)
    updated_date = models.DateTimeField('UpdatedDate',auto_now = True)
    updated_by = models.CharField('UpdatedBy',max_length=256,null=True, blank=True)


    class Meta():
        verbose_name="openstackaccount"
        verbose_name_plural="openstackaccount"

    def __str__(self):
        return self.name
