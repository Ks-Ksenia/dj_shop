# Generated by Django 3.1.2 on 2020-12-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0113_auto_20201204_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hairclipper',
            old_name='manufacture',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='hairdryer',
            old_name='manufacture',
            new_name='country',
        ),
        migrations.AlterField(
            model_name='iron',
            name='depth',
            field=models.CharField(default='240 мм', max_length=100, verbose_name='Глубина'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='height',
            field=models.CharField(default='100 мм', max_length=100, verbose_name='Высота'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='security',
            field=models.CharField(default='12 мес.', max_length=10, verbose_name='Гарантия'),
        ),
        migrations.AlterField(
            model_name='iron',
            name='width',
            field=models.CharField(default='100 мм', max_length=100, verbose_name='Ширина'),
        ),
    ]
