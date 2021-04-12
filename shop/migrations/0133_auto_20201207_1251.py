# Generated by Django 3.1.2 on 2020-12-07 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0132_auto_20201207_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='washmachine',
            old_name='prise',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='washmachine',
            name='control',
            field=models.CharField(default='кнопки, поворотный механизм', max_length=100, verbose_name='Тип управления'),
        ),
        migrations.AlterField(
            model_name='washmachine',
            name='depth',
            field=models.CharField(default='50 см', max_length=10, verbose_name='Глубина'),
        ),
        migrations.AlterField(
            model_name='washmachine',
            name='height',
            field=models.CharField(default='85 см', max_length=10, verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='washmachine',
            name='max_press',
            field=models.CharField(default='1000 об/мин', max_length=15, verbose_name='Мах скорость отжима'),
        ),
        migrations.AlterField(
            model_name='washmachine',
            name='max_time_postponement',
            field=models.CharField(default='24 ч', max_length=10, verbose_name='Мах вр отсрочки запуска'),
        ),
        migrations.AlterField(
            model_name='washmachine',
            name='number_programs',
            field=models.CharField(default='14', max_length=10, verbose_name='Кол-во программ стирки'),
        ),
        migrations.AlterField(
            model_name='washmachine',
            name='width',
            field=models.CharField(default='59.5 см', max_length=10, verbose_name='Ширина'),
        ),
    ]
