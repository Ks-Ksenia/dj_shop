# Generated by Django 3.1.2 on 2020-11-12 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0032_auto_20201110_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drymachine',
            options={'ordering': ['model'], 'verbose_name': 'Сушильные машины', 'verbose_name_plural': 'Сушильные машины'},
        ),
        migrations.RenameField(
            model_name='drymachine',
            old_name='model_name',
            new_name='category',
        ),
    ]
