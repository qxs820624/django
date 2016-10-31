from django.conf.urls import url
from school import views


urlpatterns = [
    url(r'students/$', views.students, name='students_list'),
]
