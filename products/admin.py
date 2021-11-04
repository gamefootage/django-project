from django.contrib import admin
from .models import Product, Collection


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'display_name',
        'price',
        'image_url',
        'quantities'
    )

    ordering = ('pk',)

    def quantities(self, obj):

        return f'{obj.quantity["s"] + obj.quantity["m"] + obj.quantity["l"]} \
            (s: {obj.quantity["s"]}, m: {obj.quantity["m"]}, l: {obj.quantity["l"]})'

class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'display_name'
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Collection, CollectionAdmin)