from django.db import models
from django.conf import settings

STATUS_CHOICES  = {
        ('Pending','Pending'),
        ('Active','Active'),
        ('Inactive','Inactive'),
    }

class ProgramLanguage(models.Model):
    """the product of language"""
    name = models.CharField('Language',max_length=32)

    def __str__(self):
        return self.name

class Platform(models.Model):
    """the product of platform"""
    name = models.CharField('Platform',max_length=32)

    def __str__(self):
        return self.name

class Database(models.Model):
    """the available database"""
    name = models.CharField('Database',max_length=32)

    def __str__(self):
        return self.name

class Product(models.Model):
    """products model"""
    TYPE_CHOICES  = {
        ('DBMS','DBMS'),
        ('NoSQL','NoSQL'),
        ('Artificial Intelligence','Artificial Intelligence'),
        ('HealthCare','HealthCare'),
        ('IoT','IoT'),
        ('Education','Education'),
        ('CMS','CMS'),
        ('ECOM','ECOM'),
    }
    RANK_CHOICES = {
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    }
    type = models.CharField('Type',max_length=32,default='DBMS',choices = TYPE_CHOICES)
    name = models.CharField('Name',max_length=256)
    summary = models.TextField('Summary',null=True, blank=True)
    description = models.TextField('Description',null=True, blank=True)
    detail = models.URLField('Detail',null=True,blank=True)
    product_url = models.URLField('ProductURL',max_length=256,null=True, blank=True)
    logo = models.ImageField('ProductLogo',null=True, blank=True,upload_to = 'logos/')
    vendor_name = models.CharField('VendorName',max_length=256,null=True, blank=True)
    vendor_url = models.URLField('VendorURL',max_length=256,null=True, blank=True)
    latest_version = models.CharField('LatestVersion',max_length=256,null=True, blank=True)
    first_release_date =  models.DateField('FirstReleaseDate',null=True, blank=True)
    latest_release_date =  models.DateField('LatestReleaseDate',null=True, blank=True)
    #platform
    platform =  models.ManyToManyField(Platform,blank=True)
    #language
    language = models.ManyToManyField(ProgramLanguage,blank=True)
    #database
    database = models.ManyToManyField(Database,blank=True)
    #license
    opensource = models.BooleanField('OpenSource',default=True)
    license_type = models.CharField('LicenseType',max_length=256,null=True, blank=True)
    #paid_plan
    free_plan = models.BooleanField('FreePlan',default=False)
    free_plan_spec =  models.CharField('FreePlanSpec',max_length=256,null=True, blank=True)
    paid_plan = models.BooleanField('PaidPlan',default=True)
    paid_plan_price = models.DecimalField('PaidPlanPrice',max_digits=19, decimal_places=4, null=True, blank=True)
    #demo url
    demo_url = models.URLField('DemoURL',max_length=256,null=True, blank=True)
    demo_version = models.CharField('DemoVersion',max_length=256,null=True, blank=True)
    #social url
    facebook_url  = models.URLField('FacebookURL',max_length=256,null=True, blank=True)
    facebook_follower = models.CharField('FacebookFollower',max_length=32,null=True,blank=True)
    google_plus_url = models.URLField('GoogkePlusURL',max_length=256,null=True, blank=True)
    google_plus_follower = models.CharField('GoogkePlusFollower',max_length=32,null=True,blank=True)
    linkedin_url = models.URLField('LinkedInURL',max_length=256,null=True, blank=True)
    linkedin_follower = models.CharField("LinkedInFollower",max_length=32,null=True,blank=True)
    twitter_url  = models.URLField('TwitterURL',max_length=256,null=True, blank=True)
    twitter_follower = models.CharField("TwitterFollower",max_length=32,null=True,blank=True)
    document_url = models.URLField('DocumentURL',max_length=256,null=True, blank=True)
    rank = models.IntegerField('Rank',default=5,choices=RANK_CHOICES)
    clients = models.CharField("Client",max_length=32,null=True,blank=True)
    is_popular = models.BooleanField('Popular',default=False)
    is_featured = models.BooleanField('Featured',default=False)
    special = models.CharField("Special",max_length=1024,null=True,blank=True)
    status = models.CharField('Status',max_length=32,default='Pending',choices=STATUS_CHOICES)
    created_date = models.DateTimeField('CreatedDate',auto_now_add=True)
    created_by = models.CharField('CreatedBy',max_length=32,null=True, blank=True)
    updated_date  = models.DateTimeField('UpdatedDate', auto_now=True)
    updated_by = models.CharField('UpdatedBy',max_length=32,null=True, blank=True)

    class Meta:
        verbose_name_plural = "Product"
        verbose_name = "Product"

    def __str__(self):
        return self.name

class ScreenShot(models.Model):
    """the model of screen shot"""
    product_id = models.ForeignKey(Product,related_name='screen_shot')
    software_version = models.CharField('SoftwareVersion',max_length=256,null = True,blank = True)
    title = models.CharField('Title',max_length=256)
    description = models.TextField('Description',null = True,blank = True)
    url = models.URLField('URL',max_length=256,null = True,blank = True)
    status = models.CharField('Status',max_length=32,default='Pending',choices=STATUS_CHOICES)
    created_date = models.DateTimeField('CreatedDate',auto_now_add=True)
    created_by = models.CharField('CreatedBy',max_length=32,null=True, blank=True)
    updated_date = models.DateTimeField('UpdatedDate', auto_now=True)
    updated_by = models.CharField('UpdatedBy',max_length=32,null=True, blank=True)

    class Meta:
        verbose_name = "ScreenShot"
        verbose_name_plural = "ScreenShot"

    def __str__(self):
        return self.title

class ProductCategories(models.Model):
    """the model of ProductCategories"""
    name = models.CharField('Name',max_length=256)
    description = models.TextField('Description',null = True,blank = True)
    feature01 = models.CharField('Feature01',max_length=256,null = True,blank = True)
    feature02 = models.CharField('Feature02',max_length=256,null = True,blank = True)
    feature03 =  models.CharField('Feature03',max_length=256,null = True,blank = True)
    feature04 =  models.CharField('Feature04',max_length=256,null = True,blank = True)
    feature05 =  models.CharField('Feature05',max_length=256,null = True,blank = True)
    feature06 =  models.CharField('Feature06',max_length=256,null = True,blank = True)
    feature07 =  models.CharField('Feature07',max_length=256,null = True,blank = True)
    feature08 =  models.CharField('Feature08',max_length=256,null = True,blank = True)
    feature09 =  models.CharField('Feature09',max_length=256,null = True,blank = True)
    feature10 =  models.CharField('Feature10',max_length=256,null = True,blank = True)
    status = models.CharField('Status',max_length=32,default='Pending',choices=STATUS_CHOICES)
    created_date = models.DateTimeField('CreatedDate',auto_now_add=True)
    created_by = models.CharField('CreatedBy',max_length=32,null=True, blank=True)
    updated_date = models.DateTimeField('UpdatedDate', auto_now=True)
    updated_by = models.CharField('UpdatedBy',max_length=32,null=True, blank=True)

    class Meta:
        verbose_name = "ProductCategories"
        verbose_name_plural = "ProductCategories"

    def __str__(self):
        return  self.name

class ProductToCategory(models.Model):
    """the model of ProductToCategory"""
    product_id  = models.OneToOneField(Product,related_name = 'ptc')
    category_id = models.ForeignKey(ProductCategories,related_name = 'pc')
    has_feature01 = models.BooleanField('HasFeature01',default=True)
    has_feature02 = models.BooleanField('HasFeature02',default=True)
    has_feature03 = models.BooleanField('HasFeature03',default=True)
    has_feature04 = models.BooleanField('HasFeature04',default=True)
    has_feature05 = models.BooleanField('HasFeature05',default=True)
    has_feature06 = models.BooleanField('HasFeature06',default=True)
    has_feature07 = models.BooleanField('HasFeature07',default=True)
    has_feature08 = models.BooleanField('HasFeature08',default=True)
    has_feature09 = models.BooleanField('HasFeature09',default=True)
    has_feature10 = models.BooleanField('HasFeature10',default=True)

    class Meta:
        verbose_name = 'ProductToCategory'
        verbose_name_plural = "ProductToCategory"

    def __str__(self):
        return '{}-{}'.format(self.product_id.name,self.category_id.name)

class Review(models.Model):
    """the model of review"""
    RATING_CHOICES  = {
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    }
    product_id = models.ForeignKey(Product,related_name = 'review')
    rating = models.IntegerField('Rating',null=True,blank=True,default=5,choices = RATING_CHOICES)
    reviews = models.TextField('Review',null=True, blank=True)
    status = models.CharField('Status',max_length=32,default='Pending',choices=STATUS_CHOICES)
    created_date = models.DateTimeField('CreatedDate',auto_now_add = True)
    created_by = models.CharField('CreatedBy',max_length=256,null=True, blank=True)
    updated_date = models.DateTimeField('CreatedDate',auto_now = True)
    updated_by = models.CharField('UpdatedBy',max_length=256,null=True, blank=True)

    class Meta():
        verbose_name = 'review'
        verbose_name_plural = "review"

    def __str__(self):
        return self.product_id.name

class ProductVideo(models.Model):
    """the video model"""
    product_id = models.ForeignKey(Product,related_name = 'video')
    title = models.CharField("Title",max_length = 256)
    description = models.TextField('Description',null = True,blank = True)
    url = models.URLField('URL',max_length=256,null=True, blank=True)
    status = models.CharField('Status',max_length=32,default='Pending',choices=STATUS_CHOICES)
    created_date = models.DateTimeField('CreatedDate',auto_now_add = True)
    created_by = models.CharField('CreatedBy',max_length=256,null=True, blank=True)
    updated_date = models.DateTimeField('CreatedDate',auto_now = True)
    updated_by = models.CharField('UpdatedBy',max_length=256,null=True, blank=True)

    class Meta():
        verbose_name = 'Video'
        verbose_name_plural = "Video"

    def __str__(self):
        return self.title


class ReleaseHistory(models.Model):
    """product release history"""
    product = models.ForeignKey(Product,related_name='release')
    release_date = models.DateTimeField('ReleaseDate',null=True,blank=True)
    version = models.CharField("Version",max_length=32,null=True,blank=True)
    status = models.CharField('Status',max_length=32,default='Pending',choices=STATUS_CHOICES)
    created_date = models.DateTimeField('CreatedDate',auto_now_add = True)
    created_by = models.CharField('CreatedBy',max_length=256,null=True, blank=True)
    updated_date = models.DateTimeField('CreatedDate',auto_now = True)
    updated_by = models.CharField('UpdatedBy',max_length=256,null=True, blank=True)

    class Meta:
        verbose_name = 'Version'
        verbose_name_plural = 'Version'

    def __str__(self):
        return '%s-%s' %(self.product.name,self.version)