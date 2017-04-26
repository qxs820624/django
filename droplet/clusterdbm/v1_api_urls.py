"""version 1 api here """

from django.conf.urls import include,url

from rest_framework.urlpatterns import format_suffix_patterns

from applications.api_views import (FeaturedProducts,NamedProducts,PopularProducts,\
    ProductDetail,Products,RestrictedView,VideoAPIView,ReviewAPIView,ProductFeatures,ScreenshotAPIView)
from accounts.api_views import UserLoginView,UserLoginTokenAPIView
from packages.urls import *

urlpatterns = [
    url(r'^featured-products$',FeaturedProducts.as_view(), name = 'featured-products'),
    url(r'^named-products$',NamedProducts.as_view(), name = 'named-products'),
    url(r'^popular-products$',PopularProducts.as_view(), name = 'popular-products'),
    url(r'^product/(?P<pk>[0-9]+)$',ProductDetail.as_view(), name = 'product-detail'),
    url(r'^products$',Products.as_view(), name = 'popular-products'),
    url(r'^test-auth-token$', RestrictedView.as_view()),
    url(r'^account/authentication$',UserLoginTokenAPIView.as_view(),name='login'),
    url(r'^product/videos$',VideoAPIView.as_view(),name='video'),
    url(r'^product/reviews$',ReviewAPIView.as_view(),name='review'),
    url(r'^product/features$',ProductFeatures.as_view(),name="feature"),
    url(r'^product/screenshots$',ScreenshotAPIView.as_view(),name='screenshot'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
