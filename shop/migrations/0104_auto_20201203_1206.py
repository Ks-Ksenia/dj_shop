# Generated by Django 3.1.2 on 2020-12-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0103_auto_20201203_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemunit',
            name='massa',
        ),
        migrations.RemoveField(
            model_name='systemunit',
            name='storage_configuration',
        ),
        migrations.AlterField(
            model_name='headphone',
            name='cable_length',
            field=models.CharField(default='1.2 м', max_length=100, verbose_name='Длина кабеля'),
        ),
        migrations.AlterField(
            model_name='headphone',
            name='color',
            field=models.CharField(default='чёрный', max_length=100, verbose_name='Основной цвет'),
        ),
        migrations.AlterField(
            model_name='headphone',
            name='detachable_cable',
            field=models.CharField(default='нет', max_length=100, verbose_name='Отсоединяемый кабель'),
        ),
        migrations.AlterField(
            model_name='headphone',
            name='headset_function',
            field=models.CharField(default='есть', max_length=100, verbose_name='Функция гарнитуры'),
        ),
        migrations.AlterField(
            model_name='headphone',
            name='max_reproducible_frequency',
            field=models.CharField(default='20000 Гц', max_length=100, verbose_name='Мах воспроизводимая частота'),
        ),
        migrations.AlterField(
            model_name='headphone',
            name='min_reproducible_frequency',
            field=models.CharField(default='20 Гц', max_length=100, verbose_name='Мин воспроизводимая частота'),
        ),
        migrations.AlterField(
            model_name='headphone',
            name='shape_cable_plug',
            field=models.CharField(default='прямая', max_length=100, verbose_name='Форма штекера кабеля'),
        ),
        migrations.AlterField(
            model_name='headphone',
            name='type_acoustic_design',
            field=models.CharField(default='закрытые', max_length=100, verbose_name='Тип акустического оформления'),
        ),
        migrations.AlterField(
            model_name='headphone',
            name='type_wired_connection',
            field=models.CharField(default='jack 3.5 мм', max_length=100, verbose_name='Тип проводного соединения'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='HDD',
            field=models.CharField(default='256 ГБ', max_length=100, verbose_name='Общий объём жёстких дисков (HDD)'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='SSD',
            field=models.CharField(default='256 ГБ', max_length=100, verbose_name='Общий объём твердотельных накопителей (SSD)'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='battery_capacity',
            field=models.CharField(default='4810 мА*ч', max_length=100, verbose_name='Ёмкость аккумулятора мА*ч'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='core_processor',
            field=models.CharField(default='2', max_length=100, verbose_name='Кол-во ядер процессора'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='depth',
            field=models.CharField(default='363 мм', max_length=100, verbose_name='Толщина'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='frequency_RAM',
            field=models.CharField(default='1866 МГц', max_length=100, verbose_name='Частота оперативной памяти'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='height',
            field=models.CharField(default='363 мм', max_length=100, verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='massa',
            field=models.CharField(default='1.94 кг', max_length=100, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='max_thread',
            field=models.CharField(default='2', max_length=100, verbose_name='Мак число потоков'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='model_videocard',
            field=models.CharField(default='нет', max_length=100, verbose_name='Модель встроенной видеокарты'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='pixel_density',
            field=models.CharField(default='141 PPI', max_length=100, verbose_name='Плотность пикселей'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='screen_cover',
            field=models.CharField(default='матовое', max_length=100, verbose_name='Покрытие экрана'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='screen_diagonal',
            field=models.CharField(default='15.6"', max_length=100, verbose_name='Диагональ экрана'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='screen_resolution',
            field=models.CharField(default='1920x1080', max_length=100, verbose_name='Разрешение экрана'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='screen_type',
            field=models.CharField(default='TN+film', max_length=100, verbose_name='Тип экрана'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='size_RAM',
            field=models.CharField(default='8 ГБ', max_length=100, verbose_name='Размер оперативной памяти'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='storage_configuration',
            field=models.CharField(default='только SSD', max_length=100, verbose_name='Конфигурация накопителей'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='time_job',
            field=models.CharField(default='5 ч', max_length=100, verbose_name='Приблизительное время работы'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='type_RAM',
            field=models.CharField(default='DDR4', max_length=100, verbose_name='Тип оперативной памяти'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='type_battery',
            field=models.CharField(default='Li-Ion', max_length=100, verbose_name='Тип аккумулятора'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='type_graphic_accelerator',
            field=models.CharField(default='встроенный', max_length=100, verbose_name='Вид графического ускорителя'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='width',
            field=models.CharField(default='250 мм', max_length=100, verbose_name='Ширина'),
        ),
        migrations.AlterField(
            model_name='systemunit',
            name='HDD',
            field=models.CharField(default='', max_length=100, verbose_name='Суммарный объем жестких дисков (HDD)'),
        ),
        migrations.AlterField(
            model_name='systemunit',
            name='OS',
            field=models.CharField(default='без ОС', max_length=100, verbose_name='Операционная система'),
        ),
        migrations.AlterField(
            model_name='systemunit',
            name='SSD',
            field=models.CharField(default='4 ГБ', max_length=100, verbose_name='Объем твердотельного накопителя (SSD)'),
        ),
        migrations.AlterField(
            model_name='systemunit',
            name='color',
            field=models.CharField(default='чёрный', max_length=100, verbose_name='Основной цвет'),
        ),
        migrations.AlterField(
            model_name='systemunit',
            name='core_processor',
            field=models.CharField(default='2', max_length=100, verbose_name='Кол-во ядер процессора'),
        ),
        migrations.AlterField(
            model_name='systemunit',
            name='depth',
            field=models.CharField(default='50 см', max_length=100, verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='systemunit',
            name='frequency_processor',
            field=models.CharField(default='2000 МГц', max_length=100, verbose_name='Частота процессора'),
        ),
        migrations.AlterField(
            model_name='systemunit',
            name='height',
            field=models.CharField(default='50 см', max_length=100, verbose_name='Длина'),
        ),
        migrations.AlterField(
            model_name='systemunit',
            name='size_RAM',
            field=models.CharField(default='4 ГБ', max_length=100, verbose_name='Размер оперативной памяти'),
        ),
        migrations.AlterField(
            model_name='systemunit',
            name='type_RAM',
            field=models.CharField(default='DDR3', max_length=100, verbose_name='Тип оперативноё памяти'),
        ),
        migrations.AlterField(
            model_name='systemunit',
            name='type_videocard',
            field=models.CharField(default='встроенная', max_length=100, verbose_name='Тип видео карты'),
        ),
    ]
