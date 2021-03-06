# Generated by Django 3.1.2 on 2020-12-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0133_auto_20201207_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iron',
            old_name='prise',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='iron',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='massa',
            field=models.CharField(default='0.7 кг', max_length=100, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='model',
            field=models.CharField(max_length=100, verbose_name='Модель'),
        ),
    ]
