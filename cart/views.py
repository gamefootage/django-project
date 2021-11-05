""" Configure views for cart app """
from django.shortcuts import render, redirect


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
