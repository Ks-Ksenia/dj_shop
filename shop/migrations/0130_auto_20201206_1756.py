# Generated by Django 3.1.2 on 2020-12-06 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0129_auto_20201206_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kettle',
            name='autopower',
        ),
        migrations.AlterField(
            model_name='kettle',
            name='body_material',
            field=models.CharField(default='нержавеющая сталь', max_length=100, verbose_name='Материал корпуса'),
        ),
        migrations.AlterField(
            model_name='kettle',
            name='country',
            field=models.CharField(default='Китай', max_length=200, verbose_name='Страна производитель'),
        ),
        migrations.AlterField(
            model_name='kettle',
            name='security',
            field=models.CharField(default='24 мес.', max_length=10, verbose_name='Гарантия'),
        ),
        migrations.AlterField(
            model_name='kettle',
            name='voltage',
            field=models.CharField(default='220-240 В', max_length=100, verbose_name='Напряжение питания'),
        ),
        migrations.AlterField(
            model_name='kettle',
            name='volume',
            field=models.CharField(default='1.7 л', max_length=100, verbose_name='Объём'),
        ),
        migrations.AlterField(
            model_name='kettle',
            name='width',
            field=models.CharField(default='20 см', max_length=100, verbose_name='Ширина'),
        ),
    ]