""" Configure signals being sent/received inside products app """
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import Product

@receiver(post_save, sender=Product)
def update_on_save(sender, instance, created, **kwargs):
    """ Update the total when an order item is added it an order """
    instance.update_total_quality()
