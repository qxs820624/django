from django.conf.urls import include, url
from .views import SaveComments

urlpatterns = [
    url(r'^(\w+)/save/$', SaveComments, name = 'save_comments'),       
]
