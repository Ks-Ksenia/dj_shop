# Generated by Django 3.1.2 on 2020-11-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0047_drymachine_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='washmachine',
            name='category',
            field=models.CharField(default='washmachine', max_length=250, verbose_name='имя модели'),
        ),
    ]
