#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

from . views import * 
urlpatterns = [
    url(r'^create/$', Create, name = 'create_blog'),
    url(r'^modify/$', Modify, name = 'modify_blog'),
    url(r'^delete/$', Delete, name = 'delete_blog'),
    #Reverse for 'blog.articles' with arguments '(1,)' and keyword arguments '{}' not found. 0 pattern(s) tried: []
    #add (?P<blog_id>\d+)
    url(r'^article/(?P<blog_body_id>\d+)/$', Article, name = 'article'),
    url(r'^author/(?P<blog_author>\w+)/$', ArticleByAuthor, name = 'article_author'),
    url(r'^$', ShowBlogs, name = 'show_blogs'),
    url(r'^lists/', lists, name='list'),
    url(r'^news/', news, name='news'),
    url(r'^Python/', python, name='python'),
    url(r'^abouttest/', abouttest, name='abouttest'),
    url(r'^mytalk/', mytalk, name='mytalk'),
    url(r'^diary/', diary, name='diary'),
    url(r'^add_article/', add_article, name='add_article'),
    url(r'^sub_article/', sub_article, name='sub_article'),
    url(r'^del_article/(?P<blog_body_id>\d+)/$', del_article, name='del_article'),
]
