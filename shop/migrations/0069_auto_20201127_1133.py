# Generated by Django 3.1.2 on 2020-11-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0068_order_products_for_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products_for_order',
            field=models.TextField(default='', verbose_name='Продукт(ы) в корзине'),
        ),
    ]
