from django.conf.urls import url
from packages.views import Service,MakeOrder

from .api_view import PackageAPI,PackageAllAPI

urlpatterns = [
    url(r'^service/$',Service.as_view(),name='service'),
    url(r'^makeorder/$',MakeOrder.as_view(),name='makeorder'),
    url(r'^api/package/$', PackageAPI.as_view(),name="api_package" ),
    url(r'^api/package_filter$',PackageAllAPI.as_view(),name='api_package_filter'),
]
