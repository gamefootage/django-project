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
    current_cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=product_id)
    size = request.POST.get('size')

    if not size:
        messages.error(request,
        "Please specify a size before adding to cart")
        return redirect(redirect_url)

    if product_id in list(current_cart.keys()):
        if size in list(current_cart[product_id]):
            current_cart[product_id][size] += 1
        else:
            current_cart[product_id][size] = 1

        if current_cart[product_id][size] > product.quantity[size]:
            messages.error(request,
            f"Could not add item. There are only \
                {product.quantity[size]} items in this size left.")
            return redirect(redirect_url)
    else:
        current_cart[product_id] = {}
        current_cart[product_id][size] = 1

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

def edit_cart_item(request, product_id):
    """ Edit an order item in the cart """
    current_cart = request.session.get('cart', {})
    product = get_object_or_404(Product, pk=product_id)
    size = request.POST.get('size')
    prev_size = request.POST.get('prev_size')
    quantity = request.POST.get('quantity', '')

    if size:
        if prev_size:
            if size in list(current_cart[product_id].keys()):
                add_on = current_cart[product_id][prev_size]
                current_cart[product_id][size] += add_on

            else:
                current_cart[product_id][size] = {}
                current_cart[product_id][size] = \
                    current_cart[product_id][prev_size]

            del current_cart[product_id][prev_size]
        else:
            current_cart[product_id][size] = int(quantity)
    else:
        messages.error(request, "No size specified")
        return redirect(reverse('view_cart'))

    print(current_cart)
    print(product.quantity)
    if current_cart[product_id][size] > product.quantity[size]:
        messages.warning(request,
            f"""
            There is not enough items in that size available.
            Quantity set to {product.quantity[size]} instead
            """)
        current_cart[product_id][size] = product.quantity[size]

    if prev_size:
        updated_field = 'Size'
    else:
        updated_field = 'Quantity'

    request.session['cart'] = current_cart
    messages.success(request,
    f"{updated_field} of {product.display_name} updated")
    return redirect(reverse('view_cart'))
