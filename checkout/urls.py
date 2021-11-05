""" Homepage URL configuration file """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
]
