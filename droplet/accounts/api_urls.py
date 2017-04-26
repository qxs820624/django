"""this file use to define api"""

#django package here
from django.conf.urls import url

#third party package
from rest_framework.urlpatterns import format_suffix_patterns

#self define package here
from .api_views import UserList,UserDetail,CreateUserView

urlpatterns = [
    url(r'^users/$', UserList.as_view(),name = 'userlist'),
    url(r'^users/(?P<pk>[0-9]+)/$',UserDetail.as_view(),name='userdetail'),
    url(r'register/$',CreateUserView.as_view(),name='register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
