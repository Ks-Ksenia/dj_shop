# Generated by Django 3.1.2 on 2020-11-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0042_auto_20201119_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='drymachine',
            name='diagnostics_fault',
            field=models.CharField(default='t', max_length=100, verbose_name='Самодиагностика неисправностей'),
        ),
        migrations.AddField(
            model_name='drymachine',
            name='illumination',
            field=models.CharField(default='t', max_length=100, verbose_name='Подстветка барабана'),
        ),
        migrations.AddField(
            model_name='drymachine',
            name='lines_true',
            field=models.CharField(default='t', max_length=100, verbose_name='Определения наличия белья в барабане'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='No_child',
            field=models.CharField(default='t', max_length=100, verbose_name='Блокировка от детей'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='class_energy',
            field=models.CharField(db_index=True, default='drive', max_length=150, verbose_name='Класс энергопотребления'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='color',
            field=models.CharField(max_length=100, verbose_name='Основной цвет'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='control',
            field=models.CharField(default='t', max_length=100, verbose_name='Вид управления'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='cotton',
            field=models.CharField(default='t', max_length=100, verbose_name='Хлопок'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='display',
            field=models.CharField(db_index=True, default='text', max_length=50, verbose_name='Дисплей'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='fault',
            field=models.CharField(default='t', max_length=100, verbose_name='Индикация неисправностей'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='heat_pump',
            field=models.CharField(default='t', max_length=100, verbose_name='Тепловой насос'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='humidity_linen',
            field=models.CharField(default='t', max_length=100, verbose_name='Определение влажности белья'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='load_postponing',
            field=models.IntegerField(default=1, verbose_name='Продолжительность отсрочки'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='overheating',
            field=models.CharField(default='t', max_length=100, verbose_name='Защита от перегрева'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='postponing_start',
            field=models.CharField(default='t', max_length=100, verbose_name='Отсрочка старта'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='security',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Гарантия'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='sensitive_lines',
            field=models.CharField(default='t', max_length=100, verbose_name='Чувствительное бельё'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='shop',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Наличие в магазине'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='synthetics',
            field=models.CharField(default='t', max_length=100, verbose_name='Синтетика'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='type',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Тип изделия'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='wool',
            field=models.CharField(default='t', max_length=100, verbose_name='Шерсть'),
        ),
    ]
