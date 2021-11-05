""" Configure admin site for checkout """
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    """ Allow inline editing for OrderItems """
    model = OrderItem
    readonly_fields = ('total')


class OrderAdmin(admin.ModelAdmin):
    """ Configure Order admin interface """
    inlines = (OrderItemAdminInline)

    readonly_fields = ('order_number', 'date', 'total')

    fields = (
        'order_number', 'date', 'full_name', 'email', 'phone',
        'country', 'postcode', 'city', 'street_address1',
        'street_address2', 'county', 'total'
    )

    list_display = (
        'order_number', 'date', 'full_name', 'total'
    )

    ordering = ('-date')

admin.site.register(Order, OrderAdmin)
