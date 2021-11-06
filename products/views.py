"""Configure views for products app"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.db.models import Q
from .models import Product


def get_all_products(request, *args, query_str=''):
    """ View for getting all products """

    active_filters = []
    products = Product.objects.all()
    product_fields = (
        ("size", "options"),
        ("price", "range"),
        ("colours", "options"),
        ("year", "range")
    )
    field_ranges = []
    for field, filter_type in product_fields:
        if filter_type == "range":
            (min_val) = products.filter().values_list(field).order_by(field)[0]
            (max_val) = products.filter().values_list(field).order_by\
                (f'-{field}')[0]
            obj = {}
            obj['min_val'] = int(min_val[0])
            obj['max_val'] = int(max_val[0])
            obj['field'] = field
            field_ranges.append(obj)

        # if filter_type == "options":


# if request.GET:
#         for key in request.GET:
#             if "__" in key:
#                 val = request.GET.getlist(key)
#                 val[:] = [int(x) for x in val]
#                 active_filters.append(
#                     [key.split("__")[0], key.split("__")[1], val]
#                 )
#                 obj = {}
#                 obj[key] = val
#                 query = Q(**obj)
#                 products = products.filter(query)

    if request.POST:
        for key in request.POST:
            filter_type = request.POST.get("filter_type")
            filter_field = request.POST.get("filter_field")
            filter_key = request.POST.get("filter_key")
            filter_values = request.POST.get("filter_values")
            obj = {}
            obj[filter_key] = filter_values
            query = Q(**obj)
            products = products.filter(query)

    else:

        if 'q' in request.GET:
            query = request.GET['q']
            query_str = query
            if not query:
                return redirect(reverse('products'))

            queries = Q(display_name__icontains=query) | \
                Q(name__icontains=query)
            products = products.filter(queries)


    context = {
        'products': products,
        'MEDIA_URL': settings.MEDIA_URL,
        'search_term': query_str,
        'filters': product_fields,
        'field_ranges': field_ranges,
        'active_filters': active_filters
    }

    return render(request, 'products/products.html', context)

def get_product(request, product_pk):
    """ View for getting specific product """

    product = get_object_or_404(Product, pk=product_pk)
    context = {
        'product': product,
        'MEDIA_URL': settings.MEDIA_URL
    }

    return render(request, 'products/single_product.html', context)
