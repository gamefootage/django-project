""" Configure signals being sent/received inside checkout app """
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import OrderItem

@receiver(post_save, sender=OrderItem)
def update_on_save(sender, instance, created, **kwargs):
    """ Update the total when an order item is added in an order """
    instance.order.update_total()

@receiver(post_delete, sender=OrderItem)
def update_on_delete(sender, instance, **kwargs):
    """ Update the total when an order item is deleted from an order """
    instance.order.update_total()
