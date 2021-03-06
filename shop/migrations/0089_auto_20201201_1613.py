# Generated by Django 3.1.2 on 2020-12-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0088_kettle'),
    ]

    operations = [
        migrations.CreateModel(
            name='HairClipper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='hairclipper', max_length=250, verbose_name='имя модели')),
                ('url', models.SlugField(max_length=200, unique=True, verbose_name='url')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('security', models.CharField(default='12 мес.', max_length=5, verbose_name='Гарантия')),
                ('manufacture', models.CharField(max_length=200, verbose_name='Страна производитель')),
                ('type', models.CharField(default='Машинка для стрижки волос', max_length=150, verbose_name='Тип изделия')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('professional', models.CharField(max_length=100, verbose_name='Профессиональная техника')),
                ('color', models.CharField(default='чёрный', max_length=100, verbose_name='Основной цвет')),
                ('add_color', models.CharField(default='белый', max_length=100, verbose_name='Дополнительный цвет')),
                ('type_engine', models.CharField(default='вибрационный', max_length=100, verbose_name='Тип двигателя')),
                ('max_power_consumption', models.CharField(default='12 Вт', max_length=100, verbose_name='Мак потребляемая мощность')),
                ('number_attachments', models.CharField(default='4 шт', max_length=100, verbose_name='Кол-во насадок в комплекте')),
                ('width_knife', models.CharField(default='5 мм', max_length=100, verbose_name='Ширина ножа')),
                ('blade_material', models.CharField(default='нержавеющая сталь', max_length=100, verbose_name='Материал лезвий')),
                ('wet_cleaning', models.CharField(default='нет', max_length=100, verbose_name='Влажная очистка')),
                ('shaving_head', models.CharField(default='нет', max_length=100, verbose_name='Насадка для бритья')),
                ('display', models.CharField(default='нет', max_length=100, verbose_name='Дисплей')),
                ('charge_indication', models.CharField(default='нет', max_length=100, verbose_name='Индикация заряда')),
                ('food', models.CharField(default='от сети', max_length=100, verbose_name='Питание')),
                ('charging_time', models.CharField(default='2 ч', max_length=100, verbose_name='Время зарядки')),
                ('charging_USB', models.CharField(default='есть', max_length=100, verbose_name='Зарядка от USB')),
                ('width', models.CharField(default='125 мм', max_length=100, verbose_name='Ширина')),
                ('height', models.CharField(default='125 мм', max_length=100, verbose_name='Высота')),
                ('depth', models.CharField(default='125 мм', max_length=100, verbose_name='Глубина')),
                ('massa', models.CharField(default='0.789 г', max_length=100, verbose_name='Вес')),
            ],
        ),
        migrations.CreateModel(
            name='Hairdryer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='hairdryer', max_length=250, verbose_name='имя модели')),
                ('url', models.SlugField(max_length=200, unique=True, verbose_name='url')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('security', models.CharField(default='12 мес.', max_length=5, verbose_name='Гарантия')),
                ('manufacture', models.CharField(max_length=200, verbose_name='Страна производитель')),
                ('type', models.CharField(default='Фен', max_length=150, verbose_name='Тип изделия')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('professional', models.CharField(default='нет', max_length=100, verbose_name='Профессиональный фен')),
                ('color', models.CharField(default='белый', max_length=100, verbose_name='Основной цвет')),
                ('add_color', models.CharField(default='чёрный', max_length=100, verbose_name='Дополнительный цвет')),
                ('dry_capacity', models.CharField(default='1200 Вт', max_length=100, verbose_name='Мощность сушки')),
                ('temperature_regime', models.CharField(default='2', max_length=100, verbose_name='Кол-во температурных режимов')),
                ('airspeed', models.CharField(default='2', max_length=100, verbose_name='Кол-во скоростей воздушнего потока')),
                ('cord_lenght', models.CharField(default='1.5 м', max_length=100, verbose_name='Длина сетевого шнура')),
                ('cold_air_supply', models.CharField(default='нет', max_length=100, verbose_name='Подача холодного воздуха')),
                ('ionization', models.CharField(default='нет', max_length=100, verbose_name='Ионизация')),
                ('overheating_protection', models.CharField(default='есть', max_length=100, verbose_name='Защита от перегрева')),
                ('rotation_cord', models.CharField(default='нет', max_length=100, verbose_name='Вращение шнура')),
                ('folding_handle', models.CharField(default='есть', max_length=100, verbose_name='Складная ручка')),
                ('loop_hanging', models.CharField(default='есть', max_length=100, verbose_name='Петля для подвешивания')),
                ('width', models.CharField(default='65 мм', max_length=100, verbose_name='Ширина')),
                ('height', models.CharField(default='220 мм', max_length=100, verbose_name='Высота')),
                ('depth', models.CharField(default='135 мм', max_length=100, verbose_name='Глубина')),
                ('massa', models.CharField(default='270 г', max_length=100, verbose_name='Вес')),
            ],
        ),
        migrations.AlterModelOptions(
            name='fridge',
            options={'verbose_name': 'Холодильник', 'verbose_name_plural': 'Холодильники'},
        ),
        migrations.AlterModelOptions(
            name='kettle',
            options={'verbose_name': 'Электрочайник', 'verbose_name_plural': 'Электрочайники'},
        ),
        migrations.AlterModelOptions(
            name='microwaveoven',
            options={'verbose_name': 'Микроволновка', 'verbose_name_plural': 'Микроволновки'},
        ),
        migrations.AlterModelOptions(
            name='stove',
            options={'verbose_name': 'Электроплита', 'verbose_name_plural': 'Электроплиты'},
        ),
    ]
