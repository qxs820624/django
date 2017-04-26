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
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

from .models import Product,Review,ProductVideo,ScreenShot
from .serializers import (ProductSerializer,FeaturedProductSerializer,
                          NamedProductSerializer,ProductDetailSerializer,
                          ProductFeatureSerializer,ScreenshotSerializer,
                          PopularProductSerializer,ReviewSerializer,
                          VideoSerializer)
from .filters import ProductFilter

# class JSONResponse(HttpResponse):
#     """return json data"""
#
#     def __init__(self,data,**kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse,self).__init__(content,**kwargs)
#
#
# @csrf_exempt
# def api_product_list(request):
#     """list all product"""
#     if request.method == 'GET':
#         p = Product.objects.all()
#         serializer = ProductSerializer(p,many = True)
#         return JSONResponse(serializer.data)
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ProductSerializer(data=data)
#         if serializer.is_valid():
#             return JSONResponse(serializer.data,status=201)
#         return JSONResponse(serializer.errors,status=404)
#
# @csrf_exempt
# def api_product_detail(request,pk):
#     """retrieve, updata and delete a product"""
#     try:
#         p = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = ProductSerializer(p)
#         return JSONResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ProductSerializer(p,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors,status=400)
#
#     elif request.method == 'DELETE':
#         p.delete()
#         return JSONReponse(status=204)


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


class FeaturedProducts(generics.ListAPIView):
    """popular products api"""
    permission_classes = (AllowAny,)
    queryset = Product.objects.all().filter(is_featured=True)
    serializer_class = FeaturedProductSerializer
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

class NamedProducts(generics.ListAPIView):
    """search products"""
    filter_class = ProductFilter
    serializer_class = NamedProductSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset


class PopularProducts(generics.ListAPIView):
    """popular products api"""
    permission_classes = (AllowAny,)
    queryset = Product.objects.all().filter(is_popular=True)
    serializer_class = PopularProductSerializer


class ProductDetail(generics.ListAPIView):
    """product object detail """
    serializer_class = ProductDetailSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        pk = self.kwargs.get('pk',None)
        queryset = Product.objects.filter(pk=pk)
        return queryset


class Products(generics.ListAPIView):
    """all products"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)


class RestrictedView(APIView):
    """test api"""
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        data = {
            'id': request.user.id,
            'name':request.user.name,
            "detail":"I suppose you are autenticated!"
        }
        return Response(data)


class VideoAPIView(generics.ListAPIView):
    """video find by id"""
    serializer_class = VideoSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = ProductVideo.objects.all()
        q_id = self.request.query_params.get('p_id',None)
        if q_id is not None:
            queryset = queryset.filter(product_id__id=q_id)
        return queryset

class ReviewAPIView(generics.ListAPIView):
    """review api find by product id"""
    serializer_class = ReviewSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Review.objects.filter(status="active")
        p_id = self.request.query_params.get('p_id', None)
        if p_id is not None:
            queryset = queryset.filter(product_id__id = p_id)
        return queryset


class ProductFeatures(generics.ListAPIView):
    """product feature api"""
    serializer_class = ProductFeatureSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        pass


class ScreenshotAPIView(generics.ListAPIView):
    """product screenshot api """
    serializer_class = ScreenshotSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = ScreenShot.objects.all()
        p_id = self.request.query_params.get('p_id',None)
        if p_id is not None:
            queryset = queryset.filter(product_id__id=p_id)
        return queryset

