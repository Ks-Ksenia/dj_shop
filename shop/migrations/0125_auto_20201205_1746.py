# Generated by Django 3.1.2 on 2020-12-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0124_auto_20201204_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fridge',
            name='color',
        ),
        migrations.RemoveField(
            model_name='videocard',
            name='color',
        ),
        migrations.AlterField(
            model_name='fridge',
            name='cold_storage_system',
            field=models.CharField(default='No Frost', max_length=100, verbose_name='Система холодильного отделения'),
        ),
        migrations.AlterField(
            model_name='fridge',
            name='security',
            field=models.CharField(default='12 мес.', max_length=10, verbose_name='Гарантия'),
        ),
        migrations.AlterField(
            model_name='smartwatch',
            name='compatible_devices',
            field=models.CharField(default='iOS, Android', max_length=100, verbose_name='Совместимость с операционными системами'),
        ),
        migrations.AlterField(
            model_name='smartwatch',
            name='country',
            field=models.CharField(default='Китай', max_length=200, verbose_name='Страна производитель'),
        ),
        migrations.AlterField(
            model_name='smartwatch',
            name='type',
            field=models.CharField(default='Смарт-часы', max_length=150, verbose_name='Тип изделия'),
        ),
    ]
