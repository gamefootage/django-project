"""Configure views for products app"""
from django.shortcuts import render
from django.conf import settings
from .models import Product


def get_all_products(request):
    """ View for getting all products """

    products = Product.objects.all()
    context = {
        'products': products,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'products/products.html', context)
