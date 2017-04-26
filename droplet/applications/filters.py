"""the search filter module, use django_filters"""

#third party package here
from django_filters.rest_framework import FilterSet
import django_filters

#self define model here
from .models import Product

class ProductFilter(FilterSet):
    """the product filter"""
    name = django_filters.CharFilter(name="name", lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name',]
