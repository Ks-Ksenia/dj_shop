# Generated by Django 3.1.2 on 2020-12-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0095_auto_20201202_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iron',
            name='security',
            field=models.CharField(default='1 мес.', max_length=10, verbose_name='Гарантия'),
        ),
        migrations.AlterField(
            model_name='kettle',
            name='security',
            field=models.CharField(default='12 мес.', max_length=10, verbose_name='Гарантия'),
        ),
        migrations.AlterField(
            model_name='microwaveoven',
            name='security',
            field=models.CharField(default='12 мес.', max_length=10, verbose_name='Гарантия'),
        ),
        migrations.AlterField(
            model_name='stove',
            name='security',
            field=models.CharField(default='24 мес.', max_length=5, verbose_name='Гарантия'),
        ),
        migrations.AlterField(
            model_name='stove',
            name='type',
            field=models.CharField(default='электрическая плита', max_length=150, verbose_name='Тип изделия'),
        ),
        migrations.AlterField(
            model_name='washmachine',
            name='security',
            field=models.CharField(default='12 мес.', max_length=10, verbose_name='Гарантия'),
        ),
    ]
