from django.conf.urls import include,url

from .views.staff import StaffConsole,staff_order
from .views.client import ClientConsole


urlpatterns = [
    url(r'^console/$',ClientConsole,name='console'),
    url(r'^orders/$',staff_order,name='orders'),
]
