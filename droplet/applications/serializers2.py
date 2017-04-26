"""the v2 version of serialize"""

#third party method hear
from rest_framework import serializers

#self define module hear
from .models import Product

class NamedProductSerializer(serializers.ModelSerializer):
    """version 2 serialize"""
    class Meta:
        model = Product
        fields = ['id','type','name','summary','vendor_url','vendor_name','description','logo','product_url']
