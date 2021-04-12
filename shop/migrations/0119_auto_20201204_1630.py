# Generated by Django 3.1.2 on 2020-12-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0118_auto_20201204_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='tv',
            name='depth',
            field=models.CharField(default='50 см', max_length=100, verbose_name='Глубина'),
        ),
        migrations.AddField(
            model_name='tv',
            name='height',
            field=models.CharField(default='50 см', max_length=100, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='tv',
            name='massa',
            field=models.CharField(default='2 кг', max_length=100, verbose_name='Вес'),
        ),
        migrations.AddField(
            model_name='tv',
            name='width',
            field=models.CharField(default='50 см', max_length=100, verbose_name='Ширина'),
        ),
    ]