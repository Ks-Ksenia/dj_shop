# Generated by Django 3.1.2 on 2020-11-27 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0066_auto_20201127_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products_for_order',
        ),
    ]