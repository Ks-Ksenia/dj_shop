# Generated by Django 3.1.2 on 2020-12-04 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0107_auto_20201204_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fridge',
            old_name='manufacture',
            new_name='country',
        ),
    ]
