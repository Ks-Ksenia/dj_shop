# Generated by Django 3.1.2 on 2020-10-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_f'),
    ]

    operations = [
        migrations.CreateModel(
            name='DryMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(default='drymachine', max_length=250, verbose_name='имя модели')),
                ('url', models.SlugField(max_length=200, unique=True, verbose_name='url')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('type', models.CharField(db_index=True, max_length=150, verbose_name='Тип изделия')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('color', models.CharField(max_length=100, verbose_name='Основной цвет')),
                ('width', models.FloatField(verbose_name='Ширина')),
                ('height', models.FloatField(verbose_name='Высота')),
                ('depth', models.FloatField(default=29.2, verbose_name='Глубина')),
                ('massa', models.FloatField(verbose_name='Вес')),
                ('dry_type', models.CharField(db_index=True, max_length=100, verbose_name='Тип сушки')),
                ('valume', models.FloatField(default=1, verbose_name='Объём барабана')),
                ('material_valume', models.CharField(max_length=100, verbose_name='Материал барабана')),
                ('max_load', models.FloatField(default=1, verbose_name='Мак загрузка')),
                ('enegry', models.FloatField(verbose_name='Потребляемая энергия')),
                ('material_body', models.CharField(max_length=100, verbose_name='Материал корпуса')),
                ('d_hatch', models.IntegerField(default=1, verbose_name='Диаметр загрузочного люка')),
                ('control', models.CharField(default='t', max_length=100, verbose_name='Вид управления')),
                ('display', models.CharField(db_index=True, default='text', max_length=50, verbose_name='Дисплей')),
                ('rotate', models.CharField(db_index=True, default='drive', max_length=100, verbose_name='Переменное направление вращения барабана')),
                ('class_energy', models.CharField(db_index=True, default='drive', max_length=150, verbose_name='Класс энергопотребления')),
                ('heat_pump', models.CharField(default='t', max_length=100, verbose_name='Тепловой насос')),
                ('postponing_start', models.CharField(default='t', max_length=100, verbose_name='Отсрочка старта')),
                ('load_postponing', models.IntegerField(default=1, verbose_name='Продолжительность отсрочки')),
                ('fault', models.CharField(default='t', max_length=100, verbose_name='Индикация неисправностей')),
                ('humidity_linen', models.CharField(default='t', max_length=100, verbose_name='Определение влажности белья')),
                ('lines_true', models.CharField(default='t', max_length=100, verbose_name='Определения наличия белья в барабане')),
                ('program', models.IntegerField(default=1, verbose_name='Общее кол-во программ')),
                ('cotton', models.CharField(default='t', max_length=100, verbose_name='Хлопок')),
                ('synthetics', models.CharField(default='t', max_length=100, verbose_name='Синтетика')),
                ('sensitive_lines', models.CharField(default='t', max_length=100, verbose_name='Чувствительное бельё')),
                ('wool', models.CharField(default='t', max_length=100, verbose_name='Шерсть')),
                ('No_child', models.CharField(default='t', max_length=100, verbose_name='Блокировка от детей')),
                ('overheating', models.CharField(default='t', max_length=100, verbose_name='Защита от перегрева')),
                ('diagnostics_fault', models.CharField(default='t', max_length=100, verbose_name='Самодиагностика неисправностей')),
                ('illumination', models.CharField(default='t', max_length=100, verbose_name='Подстветка барабана')),
                ('value_noice', models.IntegerField(default=1, verbose_name='Уровень шума')),
                ('shop', models.CharField(db_index=True, max_length=150, verbose_name='Наличие в магазине')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('manufacturer', models.CharField(db_index=True, max_length=100, verbose_name='Производитель')),
                ('security', models.CharField(db_index=True, max_length=100, verbose_name='Гарантия')),
            ],
            options={
                'verbose_name': 'Сушильные машины',
                'verbose_name_plural': 'Сушильные машины',
                'ordering': ['url'],
            },
        ),
        migrations.CreateModel(
            name='Iron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.SlugField(max_length=200, unique=True, verbose_name='url')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(default='iron', verbose_name='Описание')),
                ('type', models.CharField(db_index=True, default='iron', max_length=150, verbose_name='Тип изделия')),
                ('model', models.CharField(default='bosch', max_length=100, verbose_name='Модель')),
                ('color', models.CharField(default='white', max_length=100, verbose_name='Основной цвет')),
            ],
            options={
                'verbose_name': 'Утюги',
                'verbose_name_plural': 'Утюги',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=250, verbose_name='Назвение')),
                ('url', models.SlugField(max_length=150, unique=True, verbose_name='url')),
                ('body', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='WashMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.SlugField(max_length=200, unique=True, verbose_name='url')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('type', models.CharField(db_index=True, max_length=150, verbose_name='Тип изделия')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('view', models.CharField(db_index=True, max_length=100, verbose_name='Вид')),
                ('color', models.CharField(max_length=100, verbose_name='Основной цвет')),
                ('add_color', models.CharField(max_length=100, verbose_name='Дополнительный цвет')),
                ('width', models.FloatField(verbose_name='Ширина')),
                ('height', models.FloatField(verbose_name='Высота')),
                ('depth', models.FloatField(default=29.2, verbose_name='Глубина')),
                ('massa', models.FloatField(verbose_name='Вес')),
                ('upload_type', models.CharField(db_index=True, max_length=100, verbose_name='Тип загрузки')),
                ('activator', models.CharField(max_length=100, verbose_name='Активатор')),
                ('load', models.FloatField(default=1, verbose_name='Загрузка белья для стирки и отжима')),
                ('enegry', models.FloatField(verbose_name='Потребляемая энергия')),
                ('control', models.CharField(max_length=100, verbose_name='Тип управления')),
                ('temperature', models.CharField(max_length=100, verbose_name='Изменение температуры стирки')),
                ('display', models.CharField(db_index=True, default='text', max_length=50, verbose_name='Дисплей')),
                ('drive', models.CharField(db_index=True, default='drive', max_length=100, verbose_name='Прямой привод')),
                ('functional', models.CharField(db_index=True, default='drive', max_length=150, verbose_name='Функциольные особенности')),
                ('steam', models.CharField(max_length=100, verbose_name='Обработка паром')),
                ('Number_programs', models.IntegerField(verbose_name='Кол-во программ стирки')),
                ('programs', models.TextField(verbose_name='Программы')),
                ('motor', models.CharField(max_length=100, verbose_name='Инверторный двигатель')),
                ('postponement', models.CharField(max_length=100, verbose_name='Индикация')),
                ('max_time_postponement', models.CharField(max_length=100, verbose_name='Мах вр отсрочки запуска')),
                ('voice', models.CharField(max_length=100, verbose_name='Звуковой сигнал окончания стирки')),
                ('box_water', models.CharField(max_length=100, verbose_name='Бак для воды')),
                ('max_press', models.CharField(max_length=100, verbose_name='Мах скорость отжима')),
                ('choice_speed', models.CharField(max_length=100, verbose_name='Выбор скорости отжима')),
                ('voltage', models.CharField(max_length=100, verbose_name='Защита от скачков напряжения')),
                ('leak', models.CharField(max_length=100, verbose_name='Защита от просечек')),
                ('autobalance', models.CharField(max_length=100, verbose_name='Автобаланс')),
                ('No_child', models.CharField(max_length=100, verbose_name='Блокировка от детей')),
                ('class_wash', models.CharField(max_length=100, verbose_name='Класс стирки')),
                ('packaging', models.CharField(max_length=100, verbose_name='Габариты с упаковкой')),
                ('shop', models.CharField(db_index=True, max_length=150, verbose_name='Наличие в магазине')),
                ('prise', models.PositiveIntegerField(verbose_name='Цена')),
                ('manufacturer', models.CharField(db_index=True, max_length=100, verbose_name='Производитель')),
                ('security', models.CharField(db_index=True, max_length=100, verbose_name='Гарантия')),
            ],
            options={
                'verbose_name': 'Стиральные машины',
                'verbose_name_plural': 'Стиральные машины',
            },
        ),
        migrations.DeleteModel(
            name='F',
        ),
    ]
