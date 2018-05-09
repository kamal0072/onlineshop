
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^process/$', views.order_save, name='order_save'),

]