# Generated by Django 3.1.2 on 2020-11-30 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0072_auto_20201130_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drymachine',
            old_name='volume',
            new_name='valume',
        ),
    ]
