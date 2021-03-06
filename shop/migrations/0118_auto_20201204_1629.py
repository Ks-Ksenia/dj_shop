# Generated by Django 3.1.2 on 2020-12-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0117_auto_20201204_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tv',
            old_name='manufacture',
            new_name='country',
        ),
        migrations.RemoveField(
            model_name='tv',
            name='color',
        ),
        migrations.RemoveField(
            model_name='tv',
            name='depth',
        ),
        migrations.RemoveField(
            model_name='tv',
            name='height',
        ),
        migrations.RemoveField(
            model_name='tv',
            name='massa',
        ),
        migrations.RemoveField(
            model_name='tv',
            name='width',
        ),
        migrations.AlterField(
            model_name='ebook',
            name='depth',
            field=models.CharField(default='9.4 мм', max_length=100, verbose_name='Толщина'),
        ),
    ]
