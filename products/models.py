from django.db import models
from django.contrib.postgres.fields import ArrayField
from .validator import validate_quantity
import datetime


class Collection(models.Model):
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    SHIRT_SIZES = (
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large')
    )

    collection = models.ForeignKey("Collection", null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254)
    primary_colours = ArrayField(models.CharField(max_length=20), blank=True)
    player_id = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.JSONField(validators=[validate_quantity])

    def year_choices():
        return tuple((r,r) for r in range(1874, datetime.date.today().year+1))

    year = models.PositiveSmallIntegerField(choices=year_choices(), default=datetime.date.today().year)


    def __str__(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name
