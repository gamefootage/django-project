""" Configure views for cart app """
from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import resolve

from products.models import Product

def view_cart(request):
    """ Render view cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ Add a product to the cart """
    if 'redirect_url' in request.POST:
        redirect_url = request.POST.get('redirect_url')
    else:
        messages.error(
            request, "Could not find a value for redirect URL in your request"
        )
        return redirect(reverse('view_cart'))
    print(type(redirect_url))
    current_cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=product_id)

    if product_id in list(current_cart.keys()):
        current_cart[product_id] += 1
    else:
        current_cart[product_id] = 1

    if product:
        request.session['cart'] = current_cart
        messages.success(request, f'{product.display_name} added to cart')
        return redirect(redirect_url)


def remove_from_cart(request, product_id):
    """ Remove a product from the cart """
    if 'redirect_url' in request.POST:
        redirect_url = request.POST.get('redirect_url')
    else:
        messages.error(
            request, "Could not find a value for redirect URL in your request"
        )
        return redirect(reverse('view_cart'))

    current_cart = request.session.get('cart', {})

    if len(current_cart) < 1:
        messages.error(request, "Your cart seems to be empty")
        return redirect(reverse('view_cart'))
    elif product_id in current_cart:
        del current_cart[product_id]
    else:
        messages.error(request, "Could not find this item in your cart")
        return redirect(reverse('view_cart'))

    request.session['cart'] = current_cart
    return redirect(redirect_url)
