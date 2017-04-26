from django.http import HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics #basic class view
from rest_framework import mixins #mixins view
from rest_framework import status
from rest_framework import viewsets

from .models import Product
from .serializers2 import NamedProductSerializer
from .filters import ProductFilter


# @api_view(['GET','POST'])
# def featured_products(request,format=None):
#     """return featured product"""
#     if request.method == "GET":
#         featured_products = Product.objects.all().filter(is_featured=True)
#         serializer = FeaturedProductSerializer(featured_products,many = True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         data = request.POST.get('name')
#         p = Product.objects.get(name=data)
#         serializer = FeaturedProductSerializer(p)
#         return Response(serializer.data,status=status.HTTP_200_OK)

# class FeaturedProductDetail(APIView):
#     """class based api"""
#     def get_object(self,pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return Http404
#
#     def get(self, request, pk, format=None):
#         p = self.get_object(pk)
#         serializer = FeaturedProductSerializer(p)
#         return Response(serializer.data)

# class NamedProducts(generics.ListAPIView):
#     """search products"""
#     filter_class = ProductFilter
#     serializer_class = NamedProductSerializer
#
#     def get_queryset(self):
#         queryset = Product.objects.all()
#         return queryset

class NamedProducts(viewsets.ModelViewSet):
    """search product api"""
    filter_class = ProductFilter
    serializer_class = NamedProductSerializer

    def get_queryset(self):
        return Product.objects.all()


# class PopularProducts(generics.ListAPIView):
#     """popular products api"""
#     queryset = Product.objects.all().filter(is_popular=True)
#     serializer_class = PopularProductSerializer
#
#
# class ProductDetail(generics.ListAPIView):
#     """product object detail """
#     serializer_class = ProductDetailSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk',None)
#         queryset = Product.objects.filter(pk=pk)
#         return queryset
#
#
# class Products(generics.ListAPIView):
#     """all products"""
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer