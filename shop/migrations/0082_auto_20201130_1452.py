# Generated by Django 3.1.2 on 2020-11-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0081_auto_20201130_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drymachine',
            name='depth',
            field=models.CharField(default='58 см', max_length=100, verbose_name='Глубина'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='height',
            field=models.CharField(default='58 см', max_length=100, verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='load_postponing',
            field=models.CharField(default='9 ч', max_length=100, verbose_name='Продолжительность отсрочки'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='massa',
            field=models.CharField(default='58 см', max_length=100, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='max_load',
            field=models.CharField(default='8 кг', max_length=100, verbose_name='Мах загрузка'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='program',
            field=models.CharField(default='8', max_length=100, verbose_name='Общее кол-во программ'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='valume',
            field=models.CharField(default='1 л', max_length=100, verbose_name='Объём барабана'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='width',
            field=models.CharField(default='58 см', max_length=100, verbose_name='Ширина'),
        ),
    ]