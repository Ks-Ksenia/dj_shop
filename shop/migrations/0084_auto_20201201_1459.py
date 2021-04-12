# Generated by Django 3.1.2 on 2020-12-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0083_auto_20201201_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='iron',
            name='auto_shutdown',
            field=models.CharField(default='нет', max_length=100, verbose_name='Автоматическое отключение'),
        ),
        migrations.AddField(
            model_name='iron',
            name='descaling_protection',
            field=models.CharField(default='нет', max_length=100, verbose_name='Система защиты от накипи'),
        ),
        migrations.AddField(
            model_name='iron',
            name='display',
            field=models.CharField(default='нет', max_length=100, verbose_name='Дисплей'),
        ),
        migrations.AddField(
            model_name='iron',
            name='indication',
            field=models.CharField(default='нет', max_length=100, verbose_name='Индикация'),
        ),
        migrations.AddField(
            model_name='iron',
            name='power',
            field=models.CharField(default='1400 Вт', max_length=100, verbose_name='Мощность'),
        ),
        migrations.AddField(
            model_name='iron',
            name='sole_material',
            field=models.CharField(default='антипригарное покрытие', max_length=100, verbose_name='Материал подошвы'),
        ),
        migrations.AddField(
            model_name='iron',
            name='spraying',
            field=models.CharField(default='нет', max_length=100, verbose_name='Функция разбрызгивания'),
        ),
        migrations.AddField(
            model_name='iron',
            name='steam_shock',
            field=models.CharField(default='нет', max_length=100, verbose_name='Паровой удар'),
        ),
        migrations.AddField(
            model_name='iron',
            name='wireless_usage',
            field=models.CharField(default='нет', max_length=100, verbose_name='Беспроводное использование'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='color',
            field=models.CharField(default='белый', max_length=100, verbose_name='Основной цвет'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='depth',
            field=models.CharField(default='240 см', max_length=100, verbose_name='Глубина'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='height',
            field=models.CharField(default='100 см', max_length=100, verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='massa',
            field=models.CharField(default='0.700 кг', max_length=100, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='type',
            field=models.CharField(default='утюг', max_length=150, verbose_name='Тип изделия'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='width',
            field=models.CharField(default='100 см', max_length=100, verbose_name='Ширина'),
        ),
    ]
