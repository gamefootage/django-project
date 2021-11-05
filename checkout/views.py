""" Configure views for checkout app """
from django.shortcuts import render


def checkout(request):
    """ Render checkout page """
    return render(request, 'checkout/checkout.html')
