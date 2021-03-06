# Generated by Django 3.1.2 on 2020-11-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0039_auto_20201114_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drymachine',
            name='diagnostics_fault',
        ),
        migrations.RemoveField(
            model_name='drymachine',
            name='enegry',
        ),
        migrations.RemoveField(
            model_name='drymachine',
            name='illumination',
        ),
        migrations.RemoveField(
            model_name='drymachine',
            name='lines_true',
        ),
        migrations.RemoveField(
            model_name='drymachine',
            name='material_body',
        ),
        migrations.RemoveField(
            model_name='drymachine',
            name='material_valume',
        ),
        migrations.RemoveField(
            model_name='drymachine',
            name='rotate',
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='No_child',
            field=models.CharField(default='есть', max_length=100, verbose_name='Блокировка от детей'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='class_energy',
            field=models.CharField(db_index=True, default='В', max_length=150, verbose_name='Класс энергопотребления'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='color',
            field=models.CharField(default='белый', max_length=100, verbose_name='Основной цвет'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='control',
            field=models.CharField(default='кнопки', max_length=100, verbose_name='Вид управления'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='cotton',
            field=models.CharField(default='есть', max_length=100, verbose_name='Хлопок'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='display',
            field=models.CharField(db_index=True, default='есть', max_length=50, verbose_name='Дисплей'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='fault',
            field=models.CharField(default='нет', max_length=100, verbose_name='Индикация неисправностей'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='heat_pump',
            field=models.CharField(default='нет', max_length=100, verbose_name='Тепловой насос'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='humidity_linen',
            field=models.CharField(default='есть', max_length=100, verbose_name='Определение влажности белья'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='load_postponing',
            field=models.IntegerField(default=5, verbose_name='Продолжительность отсрочки'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='overheating',
            field=models.CharField(default='нет', max_length=100, verbose_name='Защита от перегрева'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='postponing_start',
            field=models.CharField(default='есть', max_length=100, verbose_name='Отсрочка старта'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='security',
            field=models.CharField(db_index=True, default='1', max_length=100, verbose_name='Гарантия'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='sensitive_lines',
            field=models.CharField(default='нет', max_length=100, verbose_name='Чувствительное бельё'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='shop',
            field=models.CharField(db_index=True, default='есть', max_length=150, verbose_name='Наличие в магазине'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='synthetics',
            field=models.CharField(default='нет', max_length=100, verbose_name='Синтетика'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='type',
            field=models.CharField(db_index=True, default='сушильная машина', max_length=150, verbose_name='Тип изделия'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='wool',
            field=models.CharField(default='нет', max_length=100, verbose_name='Шерсть'),
        ),
    ]
