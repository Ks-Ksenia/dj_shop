# Generated by Django 3.1.2 on 2020-12-04 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0109_auto_20201204_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kettle',
            old_name='manufacture',
            new_name='country',
        ),
    ]
