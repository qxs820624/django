from django.db import models
from django.conf import settings
from applications.models import Product

# Create your models here.

STATUS_CHOICES  = {
        ('Pending','Pending'),
        ('Active','Active'),
        ('Inactive','Inactive'),
    }

class Plan(models.Model):
    """plan model"""
    TYPE_CHOICES  = {
        ('Windows','Windows'),
        ('Linux','Linux'),
    }
    type = models.CharField('Type',max_length = 32,default='Linux',choices=TYPE_CHOICES)
    name = models.CharField('Name',max_length = 256)
    description = models.TextField('Description',null = True, blank = True)
    logo = models.ImageField('Logo',null=True, blank=True,upload_to = 'logos/')
    price = models.DecimalField('Price',max_digits=19, decimal_places=2)
    AWSPrice = models.DecimalField('AWSPrice',max_digits=19, decimal_places=2,null=True, blank=True)
    AzurePrice = models.DecimalField('AzurePrice',max_digits=19, decimal_places=2,null=True, blank=True)
    GooglePrice = models.DecimalField('GooglePrice',max_digits=19, decimal_places=2,null=True, blank=True)
    status = models.CharField('Status',max_length=32,default='Pending',choices=STATUS_CHOICES)
    created_date = models.DateTimeField('CreatedDate',auto_now_add = True)
    created_by = models.CharField('CreatedBy',max_length=256,null=True, blank=True)
    updated_date = models.DateTimeField('CreatedDate',auto_now = True)
    updated_by = models.CharField('UpdatedBy',max_length=256,null=True, blank=True)

    class Meta():
        verbose_name = 'Plan'
        verbose_name_plural = "Plan"

    def __str__(self):
        return self.name

class CloudConsole(models.Model):
    """cloud console model"""
    name = models.CharField('Name',max_length=256)
    description = models.TextField('Description',null = True, blank = True)
    url = models.URLField('URL',null = True,blank = True)
    username = models.CharField('Username',max_length=256)
    password = models.CharField('Password',max_length=256)
    software_version = models.CharField('SoftwareVersion',max_length=256,null = True,blank =True)
    status = models.CharField('Status',max_length=32,default='Pending',choices=STATUS_CHOICES)
    created_date = models.DateTimeField('CreatedDate',auto_now_add = True)
    created_by = models.CharField('CreatedBy',max_length=256,null=True, blank=True)
    updated_date = models.DateTimeField('CreatedDate',auto_now = True)
    updated_by = models.CharField('UpdatedBy',max_length=256,null=True, blank=True)

    class Meta():
        verbose_name = 'CloudConsole'
        verbose_name_plural = "CloudConsole"

    def __str__(self):
        return self.name

class Package(models.Model):
    """the package model"""
    MEMORY_CHOICES = {
        (2,'2GB'),
        (4,'4GB'),
        (8,'8GB'),
    }

    STATUS_CHOICES  = {
        ('Pending','Pending'),
        ('Active','Active'),
        ('Canceled','Canceled'),
        ('Suspended','Suspended'),
        ('Fraud','Fraud'),
    }

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'pu')
    product_id = models.ForeignKey(Product,related_name = 'pp')
    plan_id = models.ForeignKey(Plan,related_name = 'ppid')
    name = models.CharField('Name',max_length=256)
    description = models.TextField('Description',null = True, blank = True)
    no_of_servers = models.IntegerField('NoOfServers',null = True, blank = True)
    CPUCores = models.IntegerField('CPUCores',null = True, blank = True)
    memory = models.IntegerField('Memory',default=2,choices=MEMORY_CHOICES,null = True, blank = True)
    primary_disk = models.IntegerField('PrimaryDisk',null = True, blank = True)
    secondary_disk = models.IntegerField('SecondaryDisk',null = True, blank = True)
    third_disk = models.IntegerField('ThirdDisk',null = True, blank = True)
    band_width = models.IntegerField('Bandwidth',null = True, blank = True)
    status = models.CharField('Status',max_length=32,default='Pending',choices=STATUS_CHOICES)
    comment = models.CharField('Comment',max_length=256,null=True,blank=True)
    server_name = models.CharField('ServerName',max_length=32,null=True,blank=True)
    password = models.CharField('Password',max_length=256,default='123456')
    created_date = models.DateTimeField('CreatedDate',auto_now_add = True)
    created_by = models.CharField('CreatedBy',max_length=256,null=True, blank=True)
    updated_date = models.DateTimeField('UpdatedDate',auto_now = True)
    updated_by = models.CharField('UpdatedBy',max_length=256,null=True, blank=True)

    class Meta():
        verbose_name = 'Package'
        verbose_name_plural = "Package"

    def __str__(self):
        return self.name

class Server(models.Model):
    """server model"""
    package_id = models.ForeignKey(Package,related_name = 'sp')
    console_id = models.ForeignKey(CloudConsole,related_name = 'sc')
    name = models.CharField('Name',max_length=256)
    description = models.TextField('Description',null = True, blank = True)
    instance_id = models.CharField('InstanceID',max_length=256,null = True, blank = True)
    IP = models.GenericIPAddressField('IP',null = True, blank = True)
    CPUCores = models.IntegerField('CPUCores',null = True, blank = True)
    memory = models.IntegerField('Memory',null = True, blank = True)
    primary_disk = models.IntegerField('PrimaryDisk',null = True, blank = True)
    secondary_disk = models.IntegerField('SecondaryDisk',null = True, blank = True)
    third_disk = models.IntegerField('ThirdDisk',null = True, blank = True)
    band_width = models.IntegerField('Bandwidth',null = True, blank = True)
    status = models.CharField('Status',max_length=32,default='Pending',choices=STATUS_CHOICES)
    created_date = models.DateTimeField('CreatedDate',auto_now_add = True)
    created_by = models.CharField('CreatedBy',max_length=256,null=True, blank=True)
    updated_date = models.DateTimeField('CreatedDate',auto_now = True)
    updated_by = models.CharField('UpdatedBy',max_length=256,null=True, blank=True)

    class Meta():
        verbose_name = 'Server'
        verbose_name_plural = "Server"

    def __str__(self):
        return self.name
