# Generated by Django 3.1.2 on 2020-11-10 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_remove_exorder_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exorder',
            name='buying_type',
            field=models.CharField(choices=[('self', 'Самовывоз'), ('delivery', 'Доставка')], default='self', max_length=100, verbose_name='Тип доставки'),
        ),
    ]