"""Configure models for products app"""
import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from .validator import validate_quantity


def year_choices(max_limit):
    """Return tuple of years ranging from 1874 to the year after current"""
    return tuple((r,r) for r in range(1874, max_limit))

class Collection(models.Model):
    """Configure Collection model"""
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_display_name(self):
        """Return display_name field"""
        return self.display_name


class Product(models.Model):
    """Configure Product model"""
    SHIRT_SIZES = (
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large')
    )

    collection = models.ForeignKey(
        "Collection", null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254)
    primary_colours = ArrayField(models.CharField(max_length=20), blank=True)
    player_id = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.JSONField(validators=[validate_quantity])
    quantity_options = models.IntegerField(null=True, blank=True)

    year = models.PositiveSmallIntegerField(
        choices=year_choices(datetime.date.today().year+1),
        default=datetime.date.today().year
    )

    def save(self, *args, **kwargs):
        """
        Override original save method to set the order number
        if it hasn't been set already.
        """
        total_quantity = 0
        quantity_options = ''
        for key, value in self.quantity.items():
            total_quantity += value
        for i in range(total_quantity):
            quantity_options += str(i)
        self.quantity_options = int(quantity_options)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    def get_display_name(self):
        """Return display_name field"""
        return self.display_name
