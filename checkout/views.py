""" Configure views for checkout app """
import json
import stripe
from django.shortcuts import render, redirect, reverse, get_object_or_404, \
    HttpResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.conf import settings
from cart.contexts import cart_contents
from products.models import Product

from .forms import Order, OrderForm
from .models import OrderItem


@require_POST
def cache_checkout_data(request):
    """ Cache checkout data for easy reusue """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as exc:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=exc, status=400)


def checkout(request):
    """ Render checkout page """

    if request.method == "POST":
        cart = request.session.get("cart", {})
        form_data = {
            'full_name': request.POST.get('full_name'),
            'email': request.POST.get('email'),
            'phone': request.POST.get('phone'),
            'street_address1': request.POST.get('street_address1'),
            'street_address2': request.POST.get('street_address2'),
            'city': request.POST.get('city'),
            'county': request.POST.get('county'),
            'country': request.POST.get('country'),
            'postcode': request.POST.get('postcode')
        }
        print(form_data)
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            print(order)
            for product_id, item_data in cart.items():
                for size, quantity in item_data.items():
                    try:
                        product = Product.objects.get(pk=product_id)
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_size=size,
                        )
                        print(order_item.order)
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
            print(order.order_id)
            return redirect(reverse('checkout_success', args=[order.order_id]))
        else:
            messages.error(
                request,
                ("There was an error with the information you supplied",
                "Please double check your form.")
            )
            return redirect(reverse('checkout'))

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
    print(order.orderitems)
    return render(request, 'checkout/checkout_success.html', context)
