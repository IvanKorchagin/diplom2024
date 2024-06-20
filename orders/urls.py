from django.urls import re_path,path
from . import views

app_name = 'orders'

urlpatterns = [
    re_path(r'^create/$', views.order_create, name='order_create'),
    path('my_orders/', views.user_orders, name='user_orders'),
]

