""" Configure views for checkout app """
import stripe
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from cart.contexts import cart_contents
from products.models import Product

from .forms import Order, OrderForm
from .models import OrderItem


def checkout(request):
    """ Render checkout page """

    if request.method == "POST":
        cart = request.session.get("cart", {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'streetadress1': request.POST['streetadress1'],
            'streetadress2': request.POST['streetadress2'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode']
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_pk, item_data in cart.items():
                try:
                    product = Product.objects.get(pk=item_pk)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=item_data
                        )
                        order_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        "One of the items in your order wasn't \
                            found on our database."
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save-info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success'), args=[order.order_id]
            )
        else:
            messages.error(
                request,
                ("There was an error with the information you supplied",
                "Please double check your form.")
            )

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart to checkout")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['cart_total']
        stripe_amount = round(total * 100)
        stripe.api_key = settings.STRIPE_API_KEY

        intent = stripe.PaymentIntent.create(
            amount = stripe_amount,
            currency = settings.STRIPE_CURRENCY,
            payment_method_types = [
                "card"
            ],
        )

        order_form = OrderForm()
        context = {
            'order_form': order_form,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'client_secret': intent.client_secret
        }

    return render(request, 'checkout/checkout.html', context)

def checkout_success(request, order_id):
    """ Render success page after successful checkout """
    save_info = request.session.get('save-info')
    order = get_object_or_404(Order, order_id=order_id)
    messages.success(request,
        f'Order completed! Order No: {order_id}. A confirmation \
            email has been sent to {order.email}'
    )

    if 'cart' in request.session:
        del request.session['cart']

    context = {
        'order': order
    }
    return render(request, 'checkout/checkout_success', context)
