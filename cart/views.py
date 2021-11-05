""" Configure views for cart app """
from django.shortcuts import render, redirect
from django.contrib import messages


def view_cart(request):
    """ Render view cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ Add a product to the cart """
    redirect_url = request.POST.get('redirect_url')
    current_cart = request.session.get('cart', {})

    if product_id in list(current_cart.keys()):
        current_cart[product_id] += 1
    else:
        current_cart[product_id] = 1

    request.session['cart'] = current_cart
    return redirect(redirect_url)


def remove_from_cart(request, product_id):
    """ Remove a product from the cart """
    redirect_url = request.POST.get('redirect_url')
    current_cart = request.session.get('cart', {})

    if len(current_cart) < 1:
        messages.error(request, "Your cart seems to be empty")
    elif product_id in current_cart:
        del current_cart[product_id]
    else:
        messages.error(request, "Could not find this item in your cart")

    request.session['cart'] = current_cart
    return redirect(redirect_url)
