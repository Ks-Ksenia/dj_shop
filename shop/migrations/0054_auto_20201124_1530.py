# Generated by Django 3.1.2 on 2020-11-24 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0053_auto_20201124_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drymachine',
            name='block_child',
            field=models.CharField(choices=[('True', 'есть'), ('Fasle', 'нет')], default='True', max_length=100, verbose_name='Блокировка от детей'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='heat_pump',
            field=models.CharField(choices=[('True', 'есть'), ('Fasle', 'нет')], default=None, max_length=100, null=True, verbose_name='Тепловой насос'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='max_load',
            field=models.FloatField(blank=True, default=3, null=True, verbose_name='Мах загрузка'),
        ),
    ]