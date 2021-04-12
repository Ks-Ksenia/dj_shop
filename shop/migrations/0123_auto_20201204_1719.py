# Generated by Django 3.1.2 on 2020-12-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0122_auto_20201204_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motherboard',
            old_name='manufacture',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='processor',
            old_name='manufacture',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='rammemory',
            old_name='manufacture',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='server',
            old_name='manufacture',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='videocard',
            old_name='manufacture',
            new_name='country',
        ),
        migrations.RemoveField(
            model_name='systemunit',
            name='color',
        ),
        migrations.AlterField(
            model_name='systemunit',
            name='form_factor',
            field=models.CharField(default='', max_length=100, verbose_name='Форм-фактор корпуса'),
        ),
    ]