# Generated by Django 3.1.2 on 2020-11-25 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0057_auto_20201124_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drymachine',
            name='heat_pump',
            field=models.CharField(choices=[('Yes', 'есть'), ('No', 'нет')], default='Yes', max_length=100, null=True, verbose_name='Тепловой насос'),
        ),
    ]
