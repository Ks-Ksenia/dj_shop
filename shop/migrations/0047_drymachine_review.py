# Generated by Django 3.1.2 on 2020-11-19 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0046_auto_20201119_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='drymachine',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.review'),
        ),
    ]
