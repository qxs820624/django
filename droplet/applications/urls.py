from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import redis_detail,product_list,postgresql_detail,ProductDetail
#from .api_views import api_product_detail,api_product_list,featured_products,FeaturedProductDetail

urlpatterns= (
    url(r'^redis_detail/$',redis_detail, name = 'redis_detail' ),
    url(r'^product_list/$',product_list,name = 'product_list'),
    url(r'^postgresql_detail/$',postgresql_detail,name='postgresql_detail'),
    url(r'^(\w+)/detail/$',ProductDetail.as_view(),name='product_detail'),
    #api
    # url(r'^api/product_list/$',api_product_list,name='api_product_list'),
    # url(r'api/product_detail/(?P<pk>[0-9]+)$',api_product_detail,name='api_product_detail'),
    # url(r'api/featured-products$',featured_products,name='featured_product'),
    # url(r'api/featured-products/(?P<pk>[0-9]+)$',FeaturedProductDetail.as_view(), name = 'featured_product_detail')
)

urlpatterns = format_suffix_patterns(urlpatterns)
