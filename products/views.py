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

def get_product(request, product_pk):
    """ View for getting specific product """

    product = Product.objects.get(pk=product_pk)
    context = {
        'product': product,
        'MEDIA_URL': settings.MEDIA_URL
    }
    
    return render(request, 'products/single_product.html', context)
