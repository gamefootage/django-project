""" Configure admininstration for products app """
from django.contrib import admin
from .models import Product, Collection


class ProductAdmin(admin.ModelAdmin):
    """ Configure options for Products model on admin page """
    readonly_fields = ('pk',)
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
        """ Display quantities object in user friendly way """
        return f'{obj.quantity["s"] + obj.quantity["m"] + obj.quantity["l"]}\
        (s: {obj.quantity["s"]}, m: \
        {obj.quantity["m"]}, l: {obj.quantity["l"]})'


class CollectionAdmin(admin.ModelAdmin):
    """ Configure options for Products model on admin page """
    list_display = (
        'pk',
        'name',
        'display_name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Collection, CollectionAdmin)
