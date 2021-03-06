# Generated by Django 3.1.2 on 2020-11-30 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0076_auto_20201130_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drymachine',
            name='class_energy',
            field=models.CharField(default='В', max_length=150, verbose_name='Класс энергопотребления'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='country',
            field=models.CharField(default='Турция', max_length=100, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='display',
            field=models.CharField(default='есть', max_length=50, verbose_name='Дисплей'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='dry_type',
            field=models.CharField(default='конденсационная', max_length=100, verbose_name='Тип сушки'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='heat_pump',
            field=models.CharField(default='есть', max_length=100, verbose_name='Тепловой насос'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='manufacture',
            field=models.CharField(max_length=100, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='security',
            field=models.CharField(max_length=100, verbose_name='Гарантия'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='shop',
            field=models.CharField(choices=[('есть', 'есть'), ('нет', 'нет')], default='есть', max_length=150, verbose_name='Наличие в магазине'),
        ),
    ]
