# Generated by Django 3.1.2 on 2020-12-04 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0108_auto_20201204_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='microwaveoven',
            old_name='manufacture',
            new_name='country',
        ),
    ]