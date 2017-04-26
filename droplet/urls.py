"""clusterdbm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token

import profiles.urls
import accounts.urls
import applications.urls
import comments.urls
from . import v1_api_urls
from .v2_api_urls import router

import packages.urls
import comments.urls
from .views import AboutPage,home,NetworkPage,Price
from comments.views import SaveComments
import console.urls
import blog.urls
import excel.urls

from graphene_django.views import GraphQLView

urlpatterns = [
    url(r'^cdb/$', home, name='home'),
    #url(r'^cdb/$', views.HomePage.as_view(), name='home'),
    #url(r'^cdb/host/$', views.HostPage.as_view(), name='host'),
    #url(r'^cdb/solution/$', views.SolutionPage.as_view(), name='solution'),
    #url(r'^cdb/support/$', views.SupportPage.as_view(), name='support'),
    url(r'^cdb/about/$', AboutPage.as_view(), name='about'),
    url(r'^cdb/network/$', NetworkPage.as_view(), name='network'),
    url(r'^cdb/price/$',Price.as_view(),name='price'),
    url(r'^cdb/users/', include(profiles.urls, namespace='profiles')),
    url(r'^cdb/', include(accounts.urls, namespace='accounts')),
    url(r'^cdb/product/',include(applications.urls, namespace = 'applications')),
    url(r'^cdb/admin/', include(admin.site.urls)),
    url(r'^cdb/tinymce/', include('tinymce.urls')),
    url(r'^cdb/order/',include(packages.urls,namespace='order')),
    url(r'^cdb/comments/', include('comments.urls', namespace='comments')),
    url(r'^cdb/save_comments/$', SaveComments, name = 'save_comments'),
    url(r'^cdb/api-token-auth/', obtain_jwt_token),
    url(r'^cdb/helpdesk/', include('helpdesk.urls')),
    url(r'^cdb/panel/',include('console.urls',namespace='panel')),
    url(r'^cdb/crud/',include('crudbuilder.urls',namespace='crud')),
    url(r'^cdb/graphql', GraphQLView.as_view(graphiql=True)),
    url(r'^cdb/draceditor', include('draceditor.urls',namespace='draceditor')),
    url(r'^cdb/blog/', include('blog.urls',namespace='blog')),
    url(r'^cdb/cdyd/', include('excel.urls',namespace='excel')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#api here
import accounts.api_urls
urlpatterns += [
    url(r'^cdb/user_api/',include(accounts.api_urls,namespace='user_api')),
    url(r'^cdb/v1/',include(v1_api_urls,namespace='v1')),
    url(r'^cdb/v2/',include(router.urls,namespace='v2')),
]

#rest_framework
urlpatterns += [
    url(r'^cdb/api_auth/', include('rest_framework.urls',namespace='rest_framework')),
]
