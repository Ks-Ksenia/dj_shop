# Generated by Django 3.1.2 on 2020-12-02 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0092_auto_20201201_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='BracketTV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='bracketTV', max_length=250, verbose_name='имя модели')),
                ('url', models.SlugField(max_length=200, unique=True, verbose_name='url')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('security', models.CharField(max_length=5, verbose_name='Гарантия')),
                ('manufacture', models.CharField(max_length=200, verbose_name='Страна производитель')),
                ('type', models.CharField(default='Кранштейн для телевизора', max_length=150, verbose_name='Тип изделия')),
                ('type_TV', models.CharField(default='white', max_length=100, verbose_name='Тип кронштейна')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('color', models.CharField(default='чёрный', max_length=100, verbose_name='Цвет')),
                ('adjustment', models.CharField(default='', max_length=100, verbose_name='Способ регулировки')),
                ('attachment_point', models.CharField(default='', max_length=100, verbose_name='Место крепления кронштейна')),
                ('max_load', models.CharField(default='', max_length=100, verbose_name='Мах нагрузка')),
                ('standard_mounting_dimension', models.CharField(default='', max_length=100, verbose_name='Стандарт размеров крипления обзора')),
                ('max_diagonal_screen', models.CharField(default='', max_length=100, verbose_name='Мин диагональ экрана')),
                ('min_diagonal_screen', models.CharField(default='', max_length=100, verbose_name='Мах диагональ экрана')),
                ('angle_rotation', models.CharField(default='', max_length=100, verbose_name='Угол поворота')),
                ('tilt_angle_up', models.CharField(default='', max_length=100, verbose_name='Угол наклона вверх')),
                ('tilt_angle_down', models.CharField(default='', max_length=100, verbose_name='Угол наклона вниз')),
                ('min_distance', models.CharField(default='', max_length=100, verbose_name='Мин расстояние от стены/потолка')),
                ('max_distance', models.CharField(default='', max_length=100, verbose_name='Мах расстояние от стены/потолка')),
                ('shop', models.CharField(default='есть', max_length=150, verbose_name='Наличие в магазине')),
                ('review', models.IntegerField(default=0, verbose_name='Кол-во отзывов')),
            ],
        ),
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='ebook', max_length=250, verbose_name='имя модели')),
                ('url', models.SlugField(max_length=200, unique=True, verbose_name='url')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('security', models.CharField(default='', max_length=5, verbose_name='Гарантия')),
                ('manufacture', models.CharField(max_length=200, verbose_name='Страна производитель')),
                ('type', models.CharField(default='электронная книга', max_length=150, verbose_name='Тип изделия')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('color', models.CharField(default='белый', max_length=100, verbose_name='Цвет')),
                ('disolay_diagonal', models.CharField(default='', max_length=100, verbose_name='Диагональ дисплея')),
                ('dispaly_resolution', models.CharField(default='', max_length=100, verbose_name='Разрешение дисплея')),
                ('screen_color', models.CharField(default='', max_length=100, verbose_name='Цветной экран')),
                ('display_sensor', models.CharField(default='', max_length=100, verbose_name='Сенсорный дисплей')),
                ('text', models.CharField(default='', max_length=100, verbose_name='текстовые')),
                ('graphic', models.CharField(default='', max_length=100, verbose_name='графические')),
                ('sound', models.CharField(default='', max_length=100, verbose_name='звуковые')),
                ('video', models.CharField(default='', max_length=100, verbose_name='видео')),
                ('OS', models.CharField(default='', max_length=100, verbose_name='OC')),
                ('RAM', models.CharField(default='', max_length=100, verbose_name='Оперативная память')),
                ('internal_memory', models.CharField(default='', max_length=100, verbose_name='Встроенная память')),
                ('SIM_cart', models.CharField(default='', max_length=100, verbose_name='Слот для карты памяти')),
                ('type_SIM', models.CharField(default='', max_length=100, verbose_name='Тип карты памяти')),
                ('modile_communication', models.CharField(default='', max_length=100, verbose_name='Мобильная связь')),
                ('bluetooth', models.CharField(default='', max_length=100, verbose_name='Поддержка Bluetooth')),
                ('WIFI', models.CharField(default='', max_length=100, verbose_name='Поддержка Wi-Fi')),
                ('USB', models.CharField(default='', max_length=100, verbose_name='Тип USB разъёма')),
                ('audio_jack', models.CharField(default='', max_length=100, verbose_name='Аудиоразъёмы')),
                ('battery_capacity', models.CharField(default='', max_length=100, verbose_name='Ёмкость аккумулятора')),
                ('time_job', models.CharField(default='', max_length=100, verbose_name='Время работы')),
                ('width', models.CharField(default='50 см', max_length=100, verbose_name='Ширина')),
                ('height', models.CharField(default='50 см', max_length=100, verbose_name='Высота')),
                ('depth', models.CharField(default='50 см', max_length=100, verbose_name='Глубина')),
                ('massa', models.CharField(default='50 кг', max_length=100, verbose_name='Вес')),
                ('shop', models.CharField(default='есть', max_length=150, verbose_name='Наличие в магазине')),
                ('review', models.IntegerField(default=0, verbose_name='Кол-во отзывов')),
            ],
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='tablet', max_length=250, verbose_name='имя модели')),
                ('url', models.SlugField(max_length=200, unique=True, verbose_name='url')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('security', models.CharField(default='12 мес.', max_length=5, verbose_name='Гарантия')),
                ('manufacture', models.CharField(max_length=200, verbose_name='Страна производитель')),
                ('type', models.CharField(default='планшет', max_length=150, verbose_name='Тип изделия')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('code', models.CharField(max_length=100, verbose_name='Код производителя')),
                ('year', models.CharField(default='', max_length=100, verbose_name='Год релиза')),
                ('color', models.CharField(default='white', max_length=100, verbose_name='Цвет')),
                ('body_material', models.CharField(default='white', max_length=100, verbose_name='Материал корпуса')),
                ('screen_diagonal', models.CharField(default='', max_length=100, verbose_name='Диагональ экрана')),
                ('screenresolutin', models.CharField(default='', max_length=100, verbose_name='Разрешение экрана')),
                ('screen_protection', models.CharField(default='', max_length=100, verbose_name='Защитное покрытие экрана')),
                ('screen_technology', models.CharField(default='', max_length=100, verbose_name='Технология изготовления экрана')),
                ('processor', models.CharField(default='', max_length=100, verbose_name='Модель процессора')),
                ('number_cores', models.CharField(default='', max_length=100, verbose_name='Кол-во ядер')),
                ('RAM', models.CharField(default='', max_length=100, verbose_name='Оперативная память')),
                ('internal_memory', models.CharField(default='', max_length=100, verbose_name='Встроенная память')),
                ('SIM_cart', models.CharField(default='', max_length=100, verbose_name='Слот для карты памяти')),
                ('type_SIM', models.CharField(default='', max_length=100, verbose_name='Тип карты памяти')),
                ('cellular_communication', models.CharField(default='', max_length=100, verbose_name='Модуль сотовой связи')),
                ('bluetooth', models.CharField(default='', max_length=100, verbose_name='Версия Bluetooth')),
                ('WIFI', models.CharField(default='', max_length=100, verbose_name='Поддержка Wi-Fi')),
                ('rear_camera', models.CharField(default='', max_length=100, verbose_name='Тыловая камера')),
                ('front_camera', models.CharField(default='', max_length=100, verbose_name='Фронтальная камера')),
                ('flash', models.CharField(default='', max_length=100, verbose_name='Вспышка')),
                ('battery_capacity', models.CharField(default='', max_length=100, verbose_name='Ёмкость аккумулятора')),
                ('time_job', models.CharField(default='', max_length=100, verbose_name='Время работы')),
                ('width', models.CharField(default='50 см', max_length=100, verbose_name='Ширина')),
                ('height', models.CharField(default='50 см', max_length=100, verbose_name='Высота')),
                ('depth', models.CharField(default='50 см', max_length=100, verbose_name='Глубина')),
                ('massa', models.CharField(default='50 кг', max_length=100, verbose_name='Вес')),
                ('shop', models.CharField(default='есть', max_length=150, verbose_name='Наличие в магазине')),
                ('review', models.IntegerField(default=0, verbose_name='Кол-во отзывов')),
            ],
        ),
        migrations.CreateModel(
            name='TV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='TV', max_length=250, verbose_name='имя модели')),
                ('url', models.SlugField(max_length=200, unique=True, verbose_name='url')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('security', models.CharField(default='', max_length=5, verbose_name='Гарантия')),
                ('manufacture', models.CharField(max_length=200, verbose_name='Страна производитель')),
                ('type', models.CharField(default='Телевизор', max_length=150, verbose_name='Тип изделия')),
                ('type_TV', models.CharField(default='white', max_length=100, verbose_name='Тип телевизора')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('color', models.CharField(default='чёрный', max_length=100, verbose_name='Цвет')),
                ('screen_diagonal', models.CharField(default='', max_length=100, verbose_name='Диагональ экрана')),
                ('screen_resolution', models.CharField(default='', max_length=100, verbose_name='Разрешение экрана')),
                ('screen_format', models.CharField(default='', max_length=100, verbose_name='Формат экрана')),
                ('HDTV', models.CharField(default='', max_length=100, verbose_name='Стандарт HDTV')),
                ('screen_refresh', models.CharField(default='', max_length=100, verbose_name='Частота обновления экрана')),
                ('viewing_angle', models.CharField(default='', max_length=100, verbose_name='Угол обзора')),
                ('digital_tuner', models.CharField(default='', max_length=100, verbose_name='Цифровые тюнеры')),
                ('teletext', models.CharField(default='', max_length=100, verbose_name='Телетекст')),
                ('power_sound', models.CharField(default='', max_length=100, verbose_name='Мощность звука')),
                ('subwoofer', models.CharField(default='', max_length=100, verbose_name='Сабвуфер')),
                ('number_HDMI_port', models.CharField(default='', max_length=100, verbose_name='Кол-во HDMI портов')),
                ('headphone_output', models.CharField(default='', max_length=100, verbose_name='Выход для наушников')),
                ('number_USB_port', models.CharField(default='', max_length=100, verbose_name='Кол-во USB портов')),
                ('bluetooth', models.CharField(default='', max_length=100, verbose_name='Bluetooth')),
                ('wall_mounting', models.CharField(default='', max_length=100, verbose_name='Возможность крепления на стену')),
                ('location_stand', models.CharField(default='', max_length=100, verbose_name='Раположение подставки')),
                ('width', models.CharField(default='50 см', max_length=100, verbose_name='Ширина')),
                ('height', models.CharField(default='50 см', max_length=100, verbose_name='Высота')),
                ('depth', models.CharField(default='50 см', max_length=100, verbose_name='Глубина')),
                ('massa', models.CharField(default='50 кг', max_length=100, verbose_name='Вес')),
                ('shop', models.CharField(default='есть', max_length=150, verbose_name='Наличие в магазине')),
                ('review', models.IntegerField(default=0, verbose_name='Кол-во отзывов')),
            ],
        ),
        migrations.AddField(
            model_name='fridge',
            name='review',
            field=models.IntegerField(default=0, verbose_name='Кол-во отзывов'),
        ),
        migrations.AddField(
            model_name='fridge',
            name='shop',
            field=models.CharField(default='есть', max_length=150, verbose_name='Наличие в магазине'),
        ),
        migrations.AddField(
            model_name='hairclipper',
            name='review',
            field=models.IntegerField(default=0, verbose_name='Кол-во отзывов'),
        ),
        migrations.AddField(
            model_name='hairclipper',
            name='shop',
            field=models.CharField(default='есть', max_length=150, verbose_name='Наличие в магазине'),
        ),
        migrations.AddField(
            model_name='hairdryer',
            name='review',
            field=models.IntegerField(default=0, verbose_name='Кол-во отзывов'),
        ),
        migrations.AddField(
            model_name='hairdryer',
            name='shop',
            field=models.CharField(default='есть', max_length=150, verbose_name='Наличие в магазине'),
        ),
        migrations.AddField(
            model_name='iron',
            name='prise',
            field=models.PositiveIntegerField(default=1, verbose_name='Цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='iron',
            name='review',
            field=models.IntegerField(default=0, verbose_name='Кол-во отзывов'),
        ),
        migrations.AddField(
            model_name='iron',
            name='shop',
            field=models.CharField(default='есть', max_length=150, verbose_name='Наличие в магазине'),
        ),
        migrations.AddField(
            model_name='kettle',
            name='review',
            field=models.IntegerField(default=0, verbose_name='Кол-во отзывов'),
        ),
        migrations.AddField(
            model_name='kettle',
            name='shop',
            field=models.CharField(default='есть', max_length=150, verbose_name='Наличие в магазине'),
        ),
        migrations.AddField(
            model_name='microwaveoven',
            name='review',
            field=models.IntegerField(default=0, verbose_name='Кол-во отзывов'),
        ),
        migrations.AddField(
            model_name='microwaveoven',
            name='shop',
            field=models.CharField(default='есть', max_length=150, verbose_name='Наличие в магазине'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='review',
            field=models.IntegerField(default=0, verbose_name='Кол-во отзывов'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='shop',
            field=models.CharField(default='есть', max_length=150, verbose_name='Наличие в магазине'),
        ),
        migrations.AddField(
            model_name='smartwatch',
            name='review',
            field=models.IntegerField(default=0, verbose_name='Кол-во отзывов'),
        ),
        migrations.AddField(
            model_name='smartwatch',
            name='shop',
            field=models.CharField(default='есть', max_length=150, verbose_name='Наличие в магазине'),
        ),
        migrations.AddField(
            model_name='stove',
            name='review',
            field=models.IntegerField(default=0, verbose_name='Кол-во отзывов'),
        ),
        migrations.AddField(
            model_name='stove',
            name='shop',
            field=models.CharField(default='есть', max_length=150, verbose_name='Наличие в магазине'),
        ),
        migrations.AlterField(
            model_name='smartwatch',
            name='category',
            field=models.CharField(default='smartwatch', max_length=250, verbose_name='имя модели'),
        ),
    ]
