# Generated by Django 3.1.2 on 2020-11-13 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0034_remove_review_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['id'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(max_length=10000, verbose_name='Отзыв'),
        ),
    ]