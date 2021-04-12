# Generated by Django 3.1.2 on 2020-10-27 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_remove_exorder_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='exorder',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_order', to='shop.CartProduct', verbose_name='Продукт(ы) в корзине'),
        ),
    ]