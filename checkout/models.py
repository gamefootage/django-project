""" Configure checkout models """
import uuid
from django.db import models
from django.db.models import Sum

from products.models import Product


class Order(models.Model):
    """ Define Order model """
    order_id = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, \
        null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False,
        blank=False, default='')

    def update_total(self):
        """ Update the total to match the order items combined """
        self.total = self.orderitems.aggregate(
            Sum('orderitem_total')
        )['orderitem_total__sum']

    def _generate_order_id(self):
        """ Generate an order number using UUID """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_id:
            self.order_id = self._generate_order_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id


class OrderItem(models.Model):
    """ Define OrderItem model """
    order = models.ForeignKey(Order, null=False, blank=False, \
        on_delete=models.CASCADE, related_name='orderitems')
    product = models.ForeignKey(Product, null=False, blank=False, \
        on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    orderitem_total = models.DecimalField(max_digits=6, decimal_places=2, \
        null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.orderitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'ID {self.product.pk} on order \
            {self.order.order_id}'
