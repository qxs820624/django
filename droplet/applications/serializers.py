import datetime

from rest_framework import serializers

from .models import Product,STATUS_CHOICES,ProductVideo,Review,ScreenShot
from packages.models import Package

class ProductSerializer(serializers.ModelSerializer):
    """product serializes"""
    class Meta:
        model = Product
        fields = ["id", "name", "logo", "type","product_url"]


class ProductDetailSerializer(serializers.ModelSerializer):
    """product detail serializer"""
    class Meta:
        model = Product
        fields = ['description','language','name','license_type','vendor_url','vendor_name',
                  'free_plan_spec','database',"logo", "type",'document_url','linkedin_url','facebook_url',
                  'free_plan_spec','free_plan','google_plus_url','latest_version','summary',
                  'latest_release_date','demo_url','demo_version','paid_plan',
                  'paid_plan_price','special','status','platform','opensource']


class FeaturedProductSerializer(serializers.ModelSerializer):
    """serialize featured products"""
    rank = serializers.SerializerMethodField()
    client = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ["pk","type","name", "summary", "product_url","status","rank","client","age"]

    def get_rank(self,obj):
        """return every object of rank"""
        review_list = obj.review.filter(status='active')
        #compute the average of rank
        total_rank = 0
        rank = 0
        if review_list:
            for review in review_list:
                total_rank += review.rating
                rank = total_rank/len(review_list)
        return round(rank,1) if rank else 5.0

    def get_client(self,obj):
        """the amount of client from the how many product package use"""
        query_package = Package.objects.filter(product_id__name=obj.name)
        return len(query_package)

    def get_age(self,obj):
        """the usage of year from first release date to now """
        timedelta = -1
        if obj:
            timedelta  = datetime.date.today().year - obj.first_release_date.year
        return timedelta


class NamedProductSerializer(serializers.ModelSerializer):
    """search field product serializer"""
    class Meta:
        model = Product
        fields = ['id','name']


class PopularProductSerializer(serializers.ModelSerializer):
    """popular product serializer"""
    class Meta:
        model = Product
        fields = ['id','vendor_url','vendor_name', 'description',"logo",
                  "type", "summary", "product_url",'name']


class VideoSerializer(serializers.ModelSerializer):
    """video serializer"""
    class Meta:
        model = ProductVideo
        fields = ['status','id','description','title','url']


class ReviewSerializer(serializers.ModelSerializer):
    """review serializer"""
    class Meta:
        model = Review
        fields = ['status','reviews','created_date','created_by']


class ProductFeatureSerializer(serializers.Serializer):
    """product feature serializer"""
    pass


class ScreenshotSerializer(serializers.ModelSerializer):
    """screenshot serializer class"""
    class Meta:
        model = ScreenShot
        fields = ['status','description','version','title','url']






