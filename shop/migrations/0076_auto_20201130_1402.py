# Generated by Django 3.1.2 on 2020-11-30 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0075_auto_20201130_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drymachine',
            name='width',
            field=models.CharField(default=25.6, max_length=100, verbose_name='Ширина'),
        ),
    ]
