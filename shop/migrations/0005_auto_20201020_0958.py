# Generated by Django 3.1.2 on 2020-10-20 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_mainmenu_menu_review_submenu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_menu', to='shop.mainmenu', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_submenu', to='shop.menu', verbose_name='Категория'),
        ),
    ]