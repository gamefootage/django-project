""" Configure views for checkout app """
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """ Render checkout page """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart to checkout")
        return redirect(reverse('products'))

    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JsRklHhxonCNb5yuxsy8wgL1LCYRVSfZfOguqma5VIBxePaQ16FNoYDJ4CXQEDDSISwAI0oxq7RoZHJkH8EsqNQ00T6OiKnFO',
        'stripe_client_secret': 'test secret'
    }

    return render(request, 'checkout/checkout.html', context)
