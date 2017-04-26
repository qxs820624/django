from django.conf.urls import url
from company import views


urlpatterns = [
    url(r'roles/$', views.roles, name='roles_list'),
    url(r'employees/$', views.employees, name='employees_list'),
]
