"""version 2 api here """

from django.conf.urls import include,url

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from applications.api2_views import NamedProducts

router = routers.DefaultRouter()
router.register('named-products',NamedProducts,'named-products')

# urlpatterns = [
#     # url(r'^featured-products$',featured_products, name = 'featured-products'),
#     url(r'^named-products$',NamedProducts.as_view({'get':'list'}), name = 'named-products'),
#     # url(r'^popular-products$',PopularProducts.as_view(), name = 'popular-products'),
#     # url(r'^product/(?P<pk>[0-9]+)$',ProductDetail.as_view(), name = 'product-detail'),
#     # url(r'^products$',Products.as_view(), name = 'popular-products'),
# ]

#urlpatterns = format_suffix_patterns(urlpatterns)
