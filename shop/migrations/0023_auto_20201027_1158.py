# Generated by Django 3.1.2 on 2020-10-27 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_exorder_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='owner',
            new_name='customer',
        ),
    ]