# Generated by Django 3.1.2 on 2020-11-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20201102_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='product_comment',
            field=models.TextField(null=True, verbose_name='комментарий для пробукта'),
        ),
    ]
