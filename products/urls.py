""" Products URL configuration file """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_products, name='products'),
    path('<product_pk>', views.get_product, name='get_product')
]
