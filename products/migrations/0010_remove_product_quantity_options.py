# Generated by Django 3.2.7 on 2021-11-06 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_quantity_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity_options',
        ),
    ]