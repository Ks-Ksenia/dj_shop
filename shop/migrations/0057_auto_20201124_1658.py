# Generated by Django 3.1.2 on 2020-11-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0056_auto_20201124_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drymachine',
            name='block_child',
            field=models.CharField(choices=[('Yes', 'есть'), ('No', 'нет')], default='Yes', max_length=100, verbose_name='Блокировка от детей'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='cotton',
            field=models.CharField(choices=[('Yes', 'есть'), ('No', 'нет')], default='Yes', max_length=100, verbose_name='Хлопок'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='display',
            field=models.CharField(choices=[('Yes', 'есть'), ('No', 'нет')], db_index=True, default='Yes', max_length=50, verbose_name='Дисплей'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='fault',
            field=models.CharField(choices=[('Yes', 'есть'), ('No', 'нет')], default='No', max_length=100, verbose_name='Индикация неисправностей'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='heat_pump',
            field=models.CharField(choices=[('Yes', 'есть'), ('No', 'нет')], default=None, max_length=100, null=True, verbose_name='Тепловой насос'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='humidity_linen',
            field=models.CharField(choices=[('Yes', 'есть'), ('No', 'нет')], default='Yes', max_length=100, verbose_name='Определение влажности белья'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='overheating',
            field=models.CharField(choices=[('Yes', 'есть'), ('No', 'нет')], default='Yes', max_length=100, verbose_name='Защита от перегрева'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='postponing_start',
            field=models.CharField(choices=[('Yes', 'есть'), ('No', 'нет')], default='Yes', max_length=100, verbose_name='Отсрочка старта'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='sensitive_lines',
            field=models.CharField(choices=[('Yes', 'есть'), ('No', 'нет')], default='Yes', max_length=100, verbose_name='Чувствительное бельё'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='shop',
            field=models.CharField(choices=[('Yes', 'есть'), ('No', 'нет')], db_index=True, default='Yes', max_length=150, verbose_name='Наличие в магазине'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='synthetics',
            field=models.CharField(choices=[('Yes', 'есть'), ('No', 'нет')], default='Yes', max_length=100, verbose_name='Синтетика'),
        ),
        migrations.AlterField(
            model_name='drymachine',
            name='wool',
            field=models.CharField(choices=[('Yes', 'есть'), ('No', 'нет')], default='Yes', max_length=100, verbose_name='Шерсть'),
        ),
    ]
