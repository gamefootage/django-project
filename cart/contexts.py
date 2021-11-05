""" Define bag context """
from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):
    """ Retrieve contents of cart """
    product_count = 0
    cart_items = []
    cart_total = 0
    current_cart = request.session.get('cart', {})

    for product_id, quantity in current_cart.items():
        product = get_object_or_404(Product, pk=product_id)
        cart_total += product.price * quantity
        product_count += quantity
        cart_items.append({
            "product_id": product_id,
            "quantity": quantity,
            'product': product
        })

    context = {
        'product_count': product_count,
        'cart_items': cart_items,
        'cart_total': cart_total
    }

    return context
