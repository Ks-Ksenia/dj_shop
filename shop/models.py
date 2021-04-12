from datetime import datetime

from django.db import models
from django.db.models import Sum, Count
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone
from django.conf import settings


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()

        if not email:
            raise ValueError('Укажите адрес электронной почты')
        email = self.normalize_email(email)
        user = self.model(
                        email=email,
                        is_staff=is_staff,
                        is_active=True,
                        is_superuser=is_superuser,
                        last_login=now,
                        date_joined=now,
                        **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_user(self, email, password, **extra_fields):
        user = self._create_user(email, password, False, False, **extra_fields)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', unique=True)
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('Дата создания', default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'


User = get_user_model()


class Review(models.Model):
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Отзыв', max_length=10000)
    date = models.DateTimeField('Дата создания', default=datetime.now)
    quantity = models.PositiveIntegerField('Кол-во отзывов', default=0)
# создать заново и убрать null=True
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    comment_for_product = models.TextField('комментарий для продукта', null=True)

    def __str__(self):
        return f'{self.name} для {self.comment_for_product}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['id']


class MainMenu(models.Model):
    title = models.CharField('Название', max_length=150)
    url = models.SlugField('url', unique=True)
    image = models.ImageField('Изображение')

    class Meta:
        verbose_name = 'Главное меню'
        verbose_name_plural = 'Главное меню'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # self.model_name = self.__class__.__name__.lower()
        return reverse('menu_url', kwargs={'url': self.url})


class Menu(models.Model):
    category = models.ForeignKey(MainMenu, verbose_name='Категория',
                                 on_delete=models.CASCADE, related_name='related_menu')
    title = models.CharField('Название', max_length=150)
    url = models.SlugField('url', unique=True)
    image = models.ImageField('Изображение')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('submenu_url', kwargs={'url': self.url})


class SubMenu(models.Model):
    category = models.ForeignKey(Menu, verbose_name='Категория',
                                 on_delete=models.CASCADE, related_name='related_submenu')
    title = models.CharField('Название', max_length=150)
    url = models.SlugField('url', unique=True)
    image = models.ImageField('Изображение')
    model = models.CharField('Имя модели продукта', max_length=300, blank=True, null=True, default='none')


    class Meta:
        verbose_name = 'Подменю'
        verbose_name_plural = 'Подменю'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('submenu_url', kwargs={'url': self.url, 'category': self.category})


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    order = models.ManyToManyField('Order', verbose_name='Заказ', blank=True, related_name='related_customer')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатель'

    def __str__(self):
        return str(self.user)


class Cart(models.Model):
    customer = models.ForeignKey(Customer, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField('CartProduct',
                                      verbose_name='Продукт(ы) в корзине',
                                      blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField('Кол-во продуктов', default=0)
    final_price = models.PositiveIntegerField(verbose_name='Общая цена', default=0)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return str(self.id)

    def cart_sum(self, *args, **kwargs):
        cart_final_price = self.products.aggregate(Sum('final_price'))
        cart_quantity = self.products.aggregate(Sum('quantity'))

        if cart_final_price['final_price__sum']:
            self.final_price = cart_final_price['final_price__sum']
        else:
            self.final_price = 0

        if cart_quantity['quantity__sum']:
            self.total_products = cart_quantity['quantity__sum']
        else:
            self.total_products = 0

        super().save(*args, **kwargs)


class CartProduct(models.Model):
    user = models.ForeignKey(Customer, verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)
    product_price = models.PositiveIntegerField(verbose_name='Цена продукта', default=0)
    final_price = models.PositiveIntegerField(verbose_name='Общая цена', default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
# параметры можно не писать, они по умолчанию content_type и object_id
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'

    def __str__(self):
        return f'({self.quantity}) продукт(а) {self.content_object.model} для корзины {self.cart}'

    def save(self, *args, **kwargs):
        self.final_price = self.quantity * self.content_object.price
        super().save(*args, **kwargs)


class Order(models.Model):

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выполнен')
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка')
    )
# убрать у cart null=True, blank=True
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Customer, verbose_name='Покупатель', on_delete=models.CASCADE, related_name='related_order')
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=150)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('email', max_length=50)
    address = models.TextField('Адрес доставки', max_length=1024, blank=True, null=True)
    status = models.CharField('Статус заказа', max_length=100, choices=STATUS_CHOICES, default=STATUS_NEW)
    buying_type = models.CharField('Тип доставки', max_length=100, choices=BUYING_TYPE_CHOICES, default=BUYING_TYPE_SELF)
    number = models.CharField('Номер заказа', max_length=10, unique=True)
    created_at = models.DateTimeField('Дата создание заказа', auto_now=True)
    products_for_order = models.TextField('Продукт(ы) в корзине', default='')

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Fridge(models.Model):
    category = models.CharField('имя модели', max_length=250, default='fridge')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна производитель', max_length=200)

# общие параметры
    design_type = models.CharField("Тип конструкции", max_length=100, default='полноразмерный с морозильником')
    model = models.CharField("Модель", max_length=100)
    type = models.CharField('Тип изделия', max_length=150, db_index=True, default='Холодильник')

# Основные хар-ки
    energy_consumption = models.CharField("Энергопотребление", max_length=100, default='284 кВт/год')
    freezing_power = models.CharField("Мощность замораживания", max_length=100, default='4 кг/сутки')
    cold_storage_system = models.CharField("Система холодильного отделения", max_length=100, default='No Frost')
    min_temperature_freezer_NTO = models.CharField("Мин. температура морозильной камеры/НТО", max_length=100, default='-24°')
    value_noize = models.CharField("Уровень шума", max_length=100, default='40 дБ')

# Объём
    total_useful_volume = models.CharField("Общий полезный объём", max_length=100, default='80 л')
    volume_refrigerator_compartment = models.CharField("Полезный объём холодильной камеры", max_length=100, default='80 л')
    volume_refrigerator_compartment_NTO = models.CharField("Полезный объём холодильной камеры/НТО", max_length=100, default=' 80 л')

# Конструкция
    location_freezer_NTO = models.CharField("Расположение морозильной камеры/НТО", max_length=100, default='сверху')
    material_outer_covering = models.CharField("Материал внешнего покрытия", max_length=100, default='металл')
    shelf_material = models.CharField("Материал полок", max_length=100, default='металл')
    door_opening = models.CharField("Открытие дверей", max_length=100, default='направо')

# габариты
    width = models.CharField('Ширина', max_length=100, default='50 см')
    height = models.CharField("Высота", max_length=100, default='50 см')
    depth = models.CharField('Глубина', max_length=100, default='51 см')
    massa = models.CharField("Вес", max_length=100, default='25 кг')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Холодильник'
        verbose_name_plural = 'Холодильники'

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('fridge_product_url', kwargs={'url': self.url, 'category': self.category})

    def get_model_name(self):
        return self.__class__._meta.model_name


class Stove(models.Model):
    category = models.CharField('имя модели', max_length=250, default='stove')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна производитель', max_length=200)

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='электрическая плита')
    model = models.CharField("Модель", max_length=100)

# Общие хар-ки
    total_number_burnets = models.CharField("Общие кол-во комфорок", max_length=10, default='2 шт')
    volume_oven = models.CharField("Объём духовки", max_length=10, default='24 л')
    max_power_consumption = models.CharField("Мак потребляемая мощность", max_length=10, default='3 кВт')
    supply_voltage = models.CharField("Напряжение питания", max_length=100, default='220/230 В')
    energy_consumption_class = models.CharField("Класс энергопотребления", max_length=100, default='А')
    type_management = models.CharField("Вид управления", max_length=100, default='поворотный механизм')
    display = models.CharField("Дисплей", max_length=100, default='нет')
    housing_material_coating = models.CharField("Материал/покрытие корпуса", max_length=100, default='эмаль')

# Духовка
    timer = models.CharField("Таймер", max_length=100, default='есть')
    grill = models.CharField("Гриль", max_length=100, default='есть')
    max_temperature = models.CharField("Мах температура", max_length=100, default='250°')
    oven_light = models.CharField("Подсветка духовки", max_length=100, default='нет')

# Варочная панель
    material_cover_panel = models.CharField("Материал покрытия панели", max_length=100, default='эмалированная сталь')
    induction_burners = models.CharField("Индукционные конфорки", max_length=100, default='нет')
    number_double_circuit_burners = models.CharField("Число двухконтурных конфорок", max_length=100, default='нет')
    number_three_circuit_burners = models.CharField("Число трехконтурных конфорок", max_length=100, default='нет')

# габариты
    width = models.CharField('Ширина', max_length=100, default='50 см')
    height = models.CharField("Высота", max_length=100, default='85 см')
    depth = models.CharField('Глубина', max_length=100, default='60 см')
    massa = models.CharField("Вес", max_length=100, default='50 кг')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Электроплита'
        verbose_name_plural = 'Электроплиты'

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('stove_product_url', kwargs={'url': self.url, 'category': self.category})

    def get_model_name(self):
        return self.__class__._meta.model_name


class MicrowaveOven(models.Model):
    category = models.CharField('имя модели', max_length=250, default='microwaveoven')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна производитель', max_length=200, default="Китай")

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='Микроволновая печь')
    model = models.CharField("Модель", max_length=100)

# Основные хар-ки
    power_microwaves = models.CharField("Мощность микроволн", max_length=100, default='700 Вт')
    energy_consumption = models.CharField("Энергопотребление", max_length=100, default='1150 Вт')
    internal_volume = models.CharField("Внутренний объём", max_length=100, default='20 л')
    rotary_table = models.CharField("Поворотный стол", max_length=100, default='есть')
    diameter_pan = models.CharField("Диаметр поддона", max_length=100, default='24 см')
    inner_coating_camera = models.CharField("Внутреннее покрытие камеры", max_length=100, default='эмалированная сталь')

# Режимы и функции
    programs = models.CharField("Автоматические программы приготовления", max_length=100, default='есть')
    beep = models.CharField("Отключение звукового сигнала", max_length=100, default='нет')
    start = models.CharField("Отсрочка старта", max_length=100, default='есть')

# Панель управления
    type_management = models.CharField("Вид управления", max_length=100, default='поворотный механизм')
    block_child = models.CharField("Блокировка от детей", max_length=100, default='нет')
    display = models.CharField("Дисплей", max_length=100, default='есть')
    timer = models.CharField("Таймер", max_length=100, default='90 мин')

# габариты
    width = models.CharField('Ширина', max_length=100, default='45 см')
    height = models.CharField("Высота", max_length=100, default='25 см')
    depth = models.CharField('Глубина', max_length=100, default='25 см')
    massa = models.CharField("Вес", max_length=100, default='10 кг')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Микроволновка'
        verbose_name_plural = 'Микроволновки'

    def __str__(self):
        return f'{self.model}'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('microwave_oven_product_url', kwargs={'url': self.url, 'category': self.category})

    def get_model_name(self):
        return self.__class__._meta.model_name


class Kettle(models.Model):
    category = models.CharField('имя модели', max_length=250, default='kettle')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='24 мес.')
    country = models.CharField('Страна производитель', max_length=200, default="Китай")

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='Электрочайник')
    model = models.CharField("Модель", max_length=100)

# основные хар-ки
    volume = models.CharField("Объём", max_length=100, default='1.7 л')
    power = models.CharField("Мощность", max_length=100, default='800 Вт')
    body_material = models.CharField("Материал корпуса", max_length=100, default='нержавеющая сталь')
    voltage = models.CharField("Напряжение питания", max_length=100, default='220-240 В')

# комфорт
    temperature = models.CharField("Температура нагрева воды", max_length=100, default='100°')
    light = models.CharField("Подсветка", max_length=100, default='нет')
    cord_length = models.CharField("Длина сетевого шнура", max_length=100, default='0.8 м')
    cover = models.CharField("Особенности крышки", max_length=100, default='откидная защёлкивающая крышка')

# габариты
    width = models.CharField('Ширина', max_length=100, default='20 см')
    height = models.CharField("Высота", max_length=100, default='30 см')
    depth = models.CharField('Глубина', max_length=100, default='20 см')
    massa = models.CharField("Вес", max_length=100, default='2 кг')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Электрочайник'
        verbose_name_plural = 'Электрочайники'

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('kettle_product_url', kwargs={'url': self.url, 'category': self.category})

    def get_model_name(self):
        return self.__class__._meta.model_name


class WashMachine(models.Model):
    category = models.CharField('имя модели', max_length=250, default='washmachine')

    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')
# Заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна', max_length=100)
# Общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='стиральная машина')
    model = models.CharField("Модель", max_length=100)
    view = models.CharField('Вид', max_length=100, default='автомат')
# Габариты
    width = models.CharField('Ширина', max_length=10, default='59.5 см')
    height = models.CharField("Высота", max_length=10, default='85 см')
    depth = models.CharField('Глубина', max_length=10, default='50 см')
    massa = models.CharField("Вес", max_length=10, default='29 кг')
# Основные хар-кт
    upload_type = models.CharField('Тип загрузки', max_length=20, default='фронтальная')
    load = models.CharField('Загрузка белья для стирки и отжима', max_length=10, default='1 кг')
    enegry = models.CharField("Потребляемая энергия за цикл", max_length=10, default='0.7 Вт')
    control = models.CharField("Тип управления", max_length=100, default='кнопки, поворотный механизм')
    display = models.CharField('Дисплей', max_length=50, default='есть')
    drive = models.CharField('Прямой привод', max_length=10, default='нет')
# Функциональность
    steam = models.CharField("Обработка паром", max_length=10, default='есть')
    number_programs = models.CharField("Кол-во программ стирки", max_length=10, default='14')
    programs = models.TextField("Программы")
    motor = models.CharField("Инверторный двигатель", max_length=10, default='есть')
    postponing_start = models.CharField("Отсрочка запуска", max_length=10, default='есть')
    max_time_postponement = models.CharField("Мах вр отсрочки запуска", max_length=10, default='24 ч')
    voice = models.CharField("Звуковой сигнал окончания стирки", max_length=10, default='есть')
# Отжим, безопасность, классы
    max_press = models.CharField("Мах скорость отжима", max_length=15, default='1000 об/мин')
    voltage = models.CharField("Защита от скачков напряжения", max_length=10, default='есть')
    leak = models.CharField("Защита от протечек", max_length=100, default='есть')
    no_child = models.CharField("Блокировка от детей", max_length=100, default='есть')
    class_wash = models.CharField("Класс стирки", max_length=100, default='А')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('wash_machine_product_url', kwargs={'url': self.url, 'category': self.category})

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Стиральные машины'
        verbose_name_plural = 'Стиральные машины'


class DryMachine(models.Model):
    category = models.CharField('имя модели', max_length=250, default='drymachine')

    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# Заводские данные
    country = models.CharField('Страна', max_length=100, default='Турция')
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, db_index=True, default='сушильная машина')
    manufacture = models.CharField('Производитель', max_length=100)
    model = models.CharField("Модель", max_length=100)

# основные характеристики
    dry_type = models.CharField('Тип сушки', max_length=100, default='конденсационная')
    volume = models.CharField('Объём барабана', max_length=100, default='1 л')
    max_load = models.CharField('Мах загрузка', max_length=100, default='8 кг')
    control = models.CharField("Вид управления", max_length=100, default='кнопки')
    display = models.CharField('Дисплей', max_length=50, default='есть')
    class_energy = models.CharField('Класс энергопотребления', max_length=150, default='В')
    heat_pump = models.CharField("Тепловой насос", max_length=100, default='есть')

# функции и программы
    postponing_start = models.CharField("Отсрочка старта", max_length=100, default='есть')
    load_postponing = models.CharField("Продолжительность отсрочки", max_length=100, default='9 ч')
    fault = models.CharField("Индикация неисправностей", max_length=100, default='есть')
    humidity_linen = models.CharField("Определение влажности белья", max_length=100, default='есть')
    program = models.CharField("Общее кол-во программ", max_length=100, default='8')
    cotton = models.CharField("Хлопок", max_length=100, default='есть')
    synthetics = models.CharField("Синтетика", max_length=100, default='есть')
    sensitive_lines = models.CharField("Чувствительное бельё", max_length=100, default='есть')
    wool = models.CharField("Шерсть", max_length=100, default='есть')
    # безопасность
    block_child = models.CharField("Блокировка от детей", max_length=100, default='есть')
    overheating = models.CharField("Защита от перегрева", max_length=100, default='есть')
    value_noice = models.CharField('Уровень шума', max_length=100, default='65 дБ')

    # габариты
    width = models.CharField('Ширина', max_length=100, default='58 см')
    height = models.CharField("Высота", max_length=100, default='58 см')
    depth = models.CharField('Глубина', max_length=100, default='58 см')
    massa = models.CharField("Вес", max_length=100, default='58 см')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    class Meta:
        verbose_name = 'Сушильные машины'
        verbose_name_plural = 'Сушильные машины'
        ordering = ['model']

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('dry_product_url', kwargs={'url': self.url, 'category': self.category})

class Iron(models.Model):
    category = models.CharField('имя модели', max_length=250, default='iron')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна производитель', max_length=200, default='Италия')

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='утюг')
    model = models.CharField("Модель", max_length=100)

# основные хар-ки
    power = models.CharField("Мощность", max_length=100, default='1400 Вт')
    sole_material = models.CharField("Материал подошвы", max_length=100, default='антипригарное покрытие')
    steam_shock = models.CharField("Паровой удар", max_length=100, default='нет')
    spraying = models.CharField("Функция разбрызгивания", max_length=100, default='нет')

# безопасность
    auto_shutdown = models.CharField("Автоматическое отключение", max_length=100, default='нет')
    descaling_protection = models.CharField("Система защиты от накипи", max_length=100, default='нет')

# комфорт
    wireless_usage = models.CharField("Беспроводное использование", max_length=100, default='нет')
    indication = models.CharField("Индикация", max_length=100, default='нет')
    display = models.CharField("Дисплей", max_length=100, default='нет')

# габариты
    width = models.CharField('Ширина', max_length=100, default='100 мм')
    height = models.CharField("Высота", max_length=100, default='100 мм')
    depth = models.CharField('Глубина', max_length=100, default='240 мм')
    massa = models.CharField('Вес', max_length=100, default='0.7 кг')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Утюги'
        verbose_name_plural = 'Утюги'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('iron_product_url', kwargs={'url': self.url, 'category': self.category})


class Hairdryer(models.Model):
    category = models.CharField('имя модели', max_length=250, default='hairdryer')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='24 мес.')
    country = models.CharField('Страна производитель', max_length=200, default='Китай')

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='Фен')
    professional = models.CharField("Профессиональный фен", max_length=100, default='нет')
    model = models.CharField("Модель", max_length=100)

# основные хар-ки
    dry_capacity = models.CharField("Мощность сушки", max_length=100, default='1200 Вт')
    temperature_regime = models.CharField("Кол-во температурных режимов", max_length=100, default='2')
    airspeed = models.CharField("Кол-во скоростей воздушнего потока", max_length=100, default='2')
    cord_lenght = models.CharField("Длина сетевого шнура", max_length=100, default='1.5 м')

# функции и возможности
    cold_air_supply = models.CharField("Подача холодного воздуха", max_length=100, default='нет')
    ionization = models.CharField("Ионизация", max_length=100, default='нет')
    overheating_protection = models.CharField("Защита от перегрева", max_length=100, default='есть')

# конструкция
    rotation_cord = models.CharField("Вращение шнура", max_length=100, default='нет')
    folding_handle = models.CharField("Складная ручка", max_length=100, default='есть')
    loop_hanging = models.CharField("Петля для подвешивания", max_length=100, default='есть')

# габариты
    width = models.CharField('Ширина', max_length=100, default='65 мм')
    height = models.CharField("Высота", max_length=100, default='220 мм')
    depth = models.CharField('Глубина', max_length=100, default='135 мм')
    massa = models.CharField("Вес", max_length=100, default='600 г')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Фен'
        verbose_name_plural = 'Фены'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('hairdryer_product_url', kwargs={'url': self.url, 'category': self.category})


class HairClipper(models.Model):
    category = models.CharField('имя модели', max_length=250, default='hairclipper')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

    # заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна производитель', max_length=200, default="Китай")

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='Машинка для стрижки волос')
    model = models.CharField("Модель", max_length=100)
    professional = models.CharField("Профессиональная техника", max_length=100, default="нет")

# основные хар-ки
    type_engine = models.CharField("Тип двигателя", max_length=100, default='вибрационный')
    number_attachments = models.CharField("Кол-во насадок в комплекте", max_length=100, default='4 шт')
    blade_material = models.CharField("Материал лезвий", max_length=100, default='нержавеющая сталь')

# возможности, индикация
    wet_cleaning = models.CharField("Влажная очистка", max_length=100, default='нет')
    shaving_head = models.CharField("Насадка для бритья", max_length=100, default='нет')
    display = models.CharField("Дисплей", max_length=100, default='нет')
    charge_indication = models.CharField("Индикация заряда", max_length=100, default='нет')

# электропитание
    food = models.CharField("Питание", max_length=100, default='от сети/аккумулятора')
    charging_time = models.CharField("Время зарядки", max_length=100, default='8 ч')
    charging_USB = models.CharField("Зарядка от USB", max_length=100, default='есть')

# габариты
    width = models.CharField('Ширина', max_length=100, default='125 мм')
    height = models.CharField("Высота", max_length=100, default='125 мм')
    depth = models.CharField('Глубина', max_length=100, default='125 мм')
    massa = models.CharField("Вес", max_length=100, default='463 г')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Машинка для стрижки волос'
        verbose_name_plural = 'Машинки для стрижки волос'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('hair_clipper_product_url', kwargs={'url': self.url, 'category': self.category})


class Smartphone(models.Model):
    category = models.CharField('имя модели', max_length=250, default='smartphone')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна производитель', max_length=200, default="Китай")

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='Смартфон')
    model = models.CharField("Модель", max_length=100)
    year = models.CharField('Год выпуска', max_length=100)

# мобильная связь
    net_2G = models.CharField("Поддержка сетей 2G", max_length=100, default='GSM 850, GSM 1900, GSM 1800, GSM 900')
    net_3G = models.CharField("Поддержка сетей 3G", max_length=100, default='UMTS 850, UMTS 2100, UMTS 900')
    net_4G = models.CharField("Поддержка сетей 4G(LTE)", max_length=100, default='есть')
    format_SIM = models.CharField("Формат SIM-карт", max_length=100, default='Nano-SIM')
    number_SIM = models.CharField("Количество SIM-карт", max_length=100, default='2')

# экран
    screen_diagonal = models.CharField("Диагональ экрана", max_length=100, default='5.3"')
    screen_resolution = models.CharField("Разрешение экрана", max_length=100, default='1480x720')
    screen_technology = models.CharField("Технология изготовления экрана", max_length=100, default='IPS')

# Система
    OS = models.CharField("Версия ОС", max_length=100, default='Android 10')
    model_processor = models.CharField("Модель процессора", max_length=100, default='MediaTek')
    number_cores = models.CharField("Кол-во ядер", max_length=100, default='4')
    amount_RAM = models.CharField("Объём оперативной памяти", max_length=100, default='1 Гб')
    amount_internal_memory = models.CharField("Объём встроенной памяти", max_length=100, default='16 Гб')
    type_maps = models.CharField("Типы поддерживаемых карт", max_length=100, default='microSD')

# Основная(тыловая) камера
    number_camera = models.CharField("Кол-во основных(тыловых) камер", max_length=100, default='1')
    number_megapixels = models.CharField("Кол-во мегапикселей основной камеры", max_length=100, default='8 Мп')
    resolution_picture = models.CharField("Разрешение снимков", max_length=100, default='1480x720')

# видеосъёмка(основная камера)
    format_video = models.CharField("Формат видеосъёмки", max_length=100, default='Full HD')
    slow_video = models.CharField("Замедленная видеосъемка", max_length=100, default='нет')

# питание
    battery_capacity = models.CharField("Ёмкость аккумулятора", max_length=100, default='3000 мА*ч')
    time_battery = models.CharField("Время работы в режиме разговора", max_length=100, default='17 ч')

# габариты
    width = models.CharField('Ширина', max_length=100, default='125 мм')
    height = models.CharField("Высота", max_length=100, default='125 мм')
    depth = models.CharField('Толщина', max_length=100, default='7.7 мм')
    massa = models.CharField("Вес", max_length=100, default='150 г')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Смартфон'
        verbose_name_plural = 'Смартфоны'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('smartphone_product_url', kwargs={'url': self.url, 'category': self.category})


class SmartWatch(models.Model):
    category = models.CharField('имя модели', max_length=250, default='smartwatch')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна производитель', max_length=200, default="Китай")

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='Смарт-часы')
    model = models.CharField("Модель", max_length=100)
    compatible_devices = models.CharField('Совместимость с операционными системами', max_length=100, default='iOS, Android')
    type_control = models.CharField('Тип управления', max_length=100, default='сенсорное')

# дисплей
    display_availability = models.CharField("Наличие дисплея", max_length=100, default='есть')
    dial_type = models.CharField("Тип циферблата", max_length=100, default='ЖК-дисплей')
    sensor_display = models.CharField("Сенсорный дисплей", max_length=100, default='нет')
    diagonal = models.CharField("Диагональ", max_length=100, default='1.3"')
    display_form_factor = models.CharField("Форм-фактор дисплея", max_length=100, default='квадратный')

# корпус и ремешок
    degree_protection = models.CharField("Степень защиты", max_length=100, default='IP67')
    band_material = models.CharField("Материал ремешка", max_length=100, default='гипоаллергенный силикон')
    size_strap = models.CharField("Размер ремешка", max_length=100, default='регулируемый')

# Связь и коммутация
    wireless_communication = models.CharField("Беспроводная связь", max_length=100, default='Bluetooth')
    bluetooth_version = models.CharField("Версия Bluetooth", max_length=100, default='4')
    gps = models.CharField("GPS", max_length=100, default='нет')
    sim_cart = models.CharField("Слот для SIM-карты", max_length=100, default='нет')

# питание
    type_food = models.CharField("Тип питания", max_length=100, default='аккумулятор')
    battery_capacity = models.CharField("Ёмкость аккумулятора", max_length=100, default='150 мА*ч')
    time_job = models.CharField("Время работы", max_length=100, default='336 ч')

# габариты
    width = models.CharField('Ширина', max_length=100, default='125 мм')
    height = models.CharField("Высота", max_length=100, default='125 мм')
    depth = models.CharField('Толщина', max_length=100, default='125 мм')
    massa = models.CharField("Вес", max_length=100, default='33 г')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Смартчасы и браслеты'
        verbose_name_plural = 'Смартчасы и браслеты'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('smart_watch_product_url', kwargs={'url': self.url, 'category': self.category})


class Tablet(models.Model):
    category = models.CharField('имя модели', max_length=250, default='tablet')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна производитель', max_length=200, default="Китай")

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='планшет')
    model = models.CharField("Модель", max_length=100)
    code = models.CharField('Код производителя', max_length=100)
    year = models.CharField('Год релиза', max_length=100, default='')
    body_material = models.CharField("Материал корпуса", max_length=100, default='металл')

# экран
    screen_diagonal = models.CharField("Диагональ экрана", max_length=100, default='7"')
    screen_resolution = models.CharField("Разрешение экрана", max_length=100, default='1024x600')
    screen_protection = models.CharField("Защитное покрытие экрана", max_length=100, default='нет')
    screen_technology = models.CharField("Технология изготовления экрана", max_length=100, default='IPS')

# система
    processor = models.CharField("Модель процессора", max_length=100, default='')
    number_cores = models.CharField("Кол-во ядер", max_length=100, default='4')
    RAM = models.CharField("Оперативная память", max_length=100, default='2 ГБ')
    internal_memory = models.CharField("Встроенная память", max_length=100, default='32 ГБ')
    SIM_cart = models.CharField("Слот для карты памяти", max_length=100, default='есть')
    type_SIM = models.CharField("Тип карты памяти", max_length=100, default='micro SD')

# Беспроводная связь
    cellular_communication = models.CharField("Модуль сотовой связи", max_length=100, default='3G')
    WIFI = models.CharField("Поддержка Wi-Fi", max_length=100, default='есть')
    bluetooth = models.CharField("Версия Bluetooth", max_length=100, default='4.0')

# Камера
    rear_camera = models.CharField("Тыловая камера", max_length=100, default='есть')
    front_camera = models.CharField("Фронтальная камера", max_length=100, default='есть')
    flash = models.CharField("Вспышка", max_length=100, default='нет')

# питание
    battery_capacity = models.CharField("Ёмкость аккумулятора", max_length=100, default='4100 мА*ч')
    time_job = models.CharField("Время работы", max_length=100, default='14 ч')

# габариты
    width = models.CharField('Ширина', max_length=100, default='103.7 мм')
    height = models.CharField("Высота", max_length=100, default='187.6 мм')
    depth = models.CharField('Толщина', max_length=100, default='8.6 мм')
    massa = models.CharField("Вес", max_length=100, default='250 г')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Планшет'
        verbose_name_plural = 'Планшеты'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('tablet_product_url', kwargs={'url': self.url, 'category': self.category})


class EBook(models.Model):
    category = models.CharField('имя модели', max_length=250, default='ebook')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна производитель', max_length=200, default='Китай')

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='электронная книга')
    model = models.CharField("Модель", max_length=100)

# дисплей
    display_diagonal = models.CharField("Диагональ дисплея", max_length=100, default='6"')
    display_resolution = models.CharField("Разрешение дисплея", max_length=100, default='800x600')
    screen_color = models.CharField("Цветной экран", max_length=100, default='нет')
    display_sensor = models.CharField("Сенсорный дисплей", max_length=100, default='нет')

# форматы
    text = models.CharField("текстовые", max_length=100, default='MOBI, PDF, EPub, FB2, RTF, TXT, PDB')
    graphic = models.CharField("графические", max_length=100, default='PNG, GIF, BMP, JPG')
    sound = models.CharField("звуковые", max_length=100, default='нет')
    video = models.CharField("видео", max_length=100, default='нет')

# система
    OS = models.CharField("OC", max_length=100, default='')
    RAM = models.CharField("Оперативная память", max_length=100, default='128 МБ')
    internal_memory = models.CharField("Встроенная память", max_length=100, default='4 ГБ')
    SIM_cart = models.CharField("Слот для карты памяти", max_length=100, default='есть')
    type_SIM = models.CharField("Тип карты памяти", max_length=100, default='micro SDHC , micro SD')

# Беспроводная связь
    modile_communication = models.CharField("Мобильная связь", max_length=100, default='нет')
    bluetooth = models.CharField("Поддержка Bluetooth", max_length=100, default='нет')
    WIFI = models.CharField("Поддержка Wi-Fi", max_length=100, default='нет')

# разёмы и интерфейсы
    USB = models.CharField("Тип USB разъёма", max_length=100, default='micro USB')
    audio_jack = models.CharField("Аудиоразъёмы", max_length=100, default='нет')

# питание
    battery_capacity = models.CharField("Ёмкость аккумулятора", max_length=100, default='1800 мА*ч')
    time_job = models.CharField("Время работы", max_length=100, default='14 ч')

# габариты
    width = models.CharField('Ширина', max_length=100, default='116 мм')
    height = models.CharField("Высота", max_length=100, default='163.6 мм')
    depth = models.CharField('Толщина', max_length=100, default='9.4 мм')
    massa = models.CharField("Вес", max_length=100, default='148 г')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Электронная книга'
        verbose_name_plural = 'Электронные книги'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('ebook_product_url', kwargs={'url': self.url, 'category': self.category})


class TV(models.Model):
    category = models.CharField('имя модели', max_length=250, default='tv')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна производитель', max_length=200)

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='Телевизор')
    type_TV = models.CharField("Тип телевизора", max_length=100, default='телевизор LED')
    model = models.CharField("Модель", max_length=100)

# экран
    screen_diagonal = models.CharField("Диагональ экрана", max_length=100, default='22"')
    screen_resolution = models.CharField("Разрешение экрана", max_length=100, default='FullHD, 1920x1080')
    screen_format = models.CharField("Формат экрана", max_length=100, default='16:9')
    HDTV = models.CharField("Стандарт HDTV", max_length=100, default='Full HD 1080p')

# параметры матрицы
    screen_refresh = models.CharField("Частота обновления экрана", max_length=100, default='60 Гц')
    viewing_angle = models.CharField("Угол обзора", max_length=100, default='178° / 178°')

# приём сигнала
    digital_tuner = models.CharField("Цифровые тюнеры", max_length=100, default='DVB-S2 , DVB-C , DVB-T2')
    teletext = models.CharField("Телетекст", max_length=100, default='есть')

# звук
    power_sound = models.CharField("Мощность звука", max_length=100, default='60 Вт')
    subwoofer = models.CharField("Сабвуфер", max_length=100, default='нет')

# разъёмы и интерфейсы
    number_HDMI_port = models.CharField("Кол-во HDMI портов", max_length=100, default='4')
    headphone_output = models.CharField("Выход для наушников", max_length=100, default='есть')
    number_USB_port = models.CharField("Кол-во USB портов", max_length=100, default='3')
    bluetooth = models.CharField("Bluetooth", max_length=100, default='нет')

# крепление
    wall_mounting = models.CharField("Возможность крепления на стену", max_length=100, default='есть')
    location_stand = models.CharField("Раположение подставки", max_length=100, default='по бокам')

# габариты
    width = models.CharField('Ширина', max_length=100, default='50 мм')
    height = models.CharField("Высота", max_length=100, default='50 мм')
    depth = models.CharField('Толщина', max_length=100, default='50 мм')
    massa = models.CharField("Вес", max_length=100, default='53 кг')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Телевизор'
        verbose_name_plural = 'Телевизоры'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('tv_product_url', kwargs={'url': self.url, 'category': self.category})


class BracketTV(models.Model):
    category = models.CharField('имя модели', max_length=250, default='brackettv')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='Кранштейн для телевизора')
    type_TV = models.CharField("Тип кронштейна", max_length=100, default='кронштейн для ТВ')
    model = models.CharField("Модель", max_length=100)

# конструкция
    adjustment = models.CharField("Способ регулировки", max_length=100, default='наклон и поворот')
    attachment_point = models.CharField("Место крепления кронштейна", max_length=100, default='к стене')

# совместимость
    max_load = models.CharField("Мах нагрузка", max_length=100, default='25 кг')
    standard_mounting_dimension = models.CharField("Стандарт размеров крипления", max_length=100, default='100 x 100, 75 x 75')
    max_diagonal_screen = models.CharField("Мин диагональ экрана", max_length=100, default='10"')
    min_diagonal_screen = models.CharField("Мах диагональ экрана", max_length=100, default='26"')

# регулировка
    angle_rotation = models.CharField("Угол поворота ответной части", max_length=100, default='6°')
    tilt_angle_up = models.CharField("Угол наклона вверх", max_length=100, default='6°')
    tilt_angle_down = models.CharField("Угол наклона вниз", max_length=100, default='6°')
    min_distance = models.CharField("Мин расстояние от стены/потолка", max_length=100, default='21 мм')
    max_distance = models.CharField("Мах расстояние от стены/потолка", max_length=100, default='21 мм')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Кранштейн для телевизора'
        verbose_name_plural = 'Кранштейны для телевизоров'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('bracket_tv_product_url', kwargs={'url': self.url, 'category': self.category})


class Column(models.Model):
    category = models.CharField('имя модели', max_length=250, default='column')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна производитель', max_length=200, default='Китай')

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='Колонки')
    model = models.CharField("Модель", max_length=100)
    format = models.CharField("Формат системы", max_length=100, default='2.0')

# акустические хар-ки
    power = models.CharField("Мощность", max_length=100, default='20 Вт')
    min_playback_frequency = models.CharField("Мин частота воспроизведения (Гц)", max_length=100, default='60 Гц')
    max_playback_frequency = models.CharField("Мах частота воспроизведения (Гц)", max_length=100, default='20000 Гц')
    signal_noise = models.CharField("Соотношение сигнал/шум", max_length=100, default='80 дБ')

# Разъёмы и интерфейсы
    type_wired_connection = models.CharField("Тип проводного соединения", max_length=100, default='3.5 Jack')
    wireless_connection = models.CharField("Беспроводное подключение", max_length=100, default='Bluetooth')
    bluetooth = models.CharField("Версия Bluetooth", max_length=100, default='4.2')
    interface_USB = models.CharField("Интерфейс USB Type A(для флешки)", max_length=100, default='нет')
    analog_connector = models.CharField("Аналоговые разъёмы", max_length=100, default='нет')

# фронтальные колонки
    power_front_column = models.CharField("Мощность фронтальных колонок", max_length=100, default='2x10 Вт')
    material_front_column = models.CharField("Материал корпуса фронтальных колонок", max_length=100, default='пластик')
    width = models.CharField("Ширина фронтальных колонок", max_length=100, default='89 мм')
    height = models.CharField("Высота фронтальных колонок", max_length=100, default='210 мм')
    depth = models.CharField("Глубина фронтальных колонок", max_length=100, default='176 мм')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Колонки'
        verbose_name_plural = 'Колонки'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('columns_product_url', kwargs={'url': self.url, 'category': self.category})


class Headphones(models.Model):
    category = models.CharField('имя модели', max_length=250, default='headphones')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна производитель', max_length=200)

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='проводные наушники')
    model = models.CharField("Модель", max_length=100)
    gaming_headphone = models.CharField("Игровые наушники", max_length=100, default='нет')
    signal_transmission = models.CharField("Способ передачи сигнала", max_length=100, default='проводной')
    design_type = models.CharField("Тип конструкции", max_length=100, default='накладные')
    format = models.CharField("Формат звуковой схемы", max_length=100, default='2.0')
    headset_function = models.CharField("Функция гарнитуры", max_length=100, default='есть')

# акустические хар-ки
    type_acoustic_design = models.CharField("Тип акустического оформления", max_length=100, default='закрытые')
    min_reproducible_frequency = models.CharField("Мин воспроизводимая частота", max_length=100, default='20 Гц')
    max_reproducible_frequency = models.CharField("Мах воспроизводимая частота", max_length=100, default='20000 Гц')

    microphone = models.CharField("Микрофон", max_length=100, default='нет')

# проводное подключение
    type_wired_connection = models.CharField("Тип проводного соединения", max_length=100, default='jack 3.5 мм')
    detachable_cable = models.CharField("Отсоединяемый кабель", max_length=100, default='нет')
    cable_length = models.CharField("Длина кабеля", max_length=100, default='1.2 м')
    shape_cable_plug = models.CharField("Форма штекера кабеля", max_length=100, default='L-образная')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Наушники'
        verbose_name_plural = 'Наушники'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('headphones_product_url', kwargs={'url': self.url, 'category': self.category})


class Notebook(models.Model):
    category = models.CharField('имя модели', max_length=250, default='notebook')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')

# общие параметры
    type = models.CharField('Тип устройства', max_length=150, default='ноубтук')
    os = models.CharField("Операционная система", max_length=100, default='')
    model = models.CharField("Модель", max_length=100, default='')
    code = models.CharField("Код производителя", max_length=100, default='')
    year = models.CharField("Год релиза", max_length=100, default='')

# экран
    screen_type = models.CharField("Тип экрана", max_length=100, default='IPS')
    screen_diagonal = models.CharField("Диагональ экрана", max_length=100, default='15.6"')
    screen_resolution = models.CharField("Разрешение экрана", max_length=100, default='1920x1080')
    pixel_density = models.CharField("Плотность пикселей", max_length=100, default='141 PPI')
    screen_cover = models.CharField("Покрытие экрана", max_length=100, default='матовое')

# процессор
    manufacture_processor = models.CharField("Производитель процессора", max_length=100, default='Intel')
    model_processor = models.CharField("Модель процессора", max_length=100, default='')
    core_processor = models.CharField("Кол-во ядер процессора", max_length=100, default='2')
    max_thread = models.CharField("Мак число потоков", max_length=100, default='2')

# оперативная память
    type_RAM = models.CharField("Тип оперативной памяти", max_length=100, default='DDR4')
    frequency_RAM = models.CharField("Частота оперативной памяти", max_length=100, default='1866 МГц')
    size_RAM = models.CharField("Размер оперативной памяти", max_length=100, default='8 ГБ')

# графический ускоритель
    type_graphic_accelerator = models.CharField("Вид графического ускорителя", max_length=100, default='встроенный')
    manufacture_chip = models.CharField("Производитель видеочипа", max_length=100, default='nVidia')
    model_videocard = models.CharField("Модель встроенной видеокарты", max_length=100, default='нет')

# накопители данных
    HDD = models.CharField("Общий объём жёстких дисков (HDD)", max_length=100, default='256 ГБ')
    SSD = models.CharField("Общий объём твердотельных накопителей (SSD)", max_length=100, default='256 ГБ')
    storage_configuration = models.CharField("Конфигурация накопителей", max_length=100, default='только SSD')

# питание
    type_battery = models.CharField("Тип аккумулятора", max_length=100, default='Li-Ion')
    battery_capacity = models.CharField("Ёмкость аккумулятора мА*ч", max_length=100, default='4810 мА*ч')
    time_job = models.CharField("Приблизительное время работы", max_length=100, default='5 ч')

# габариты
    width = models.CharField('Ширина', max_length=100, default='250 мм')
    height = models.CharField("Высота", max_length=100, default='363 мм')
    depth = models.CharField('Толщина', max_length=100, default='36 мм')
    massa = models.CharField("Вес", max_length=100, default='1.94 кг')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('notebook_product_url', kwargs={'url': self.url, 'category': self.category})


class SystemUnit(models.Model):
    category = models.CharField('имя модели', max_length=250, default='systemunit')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')

# общие параметры
    type = models.CharField('Тип устройства', max_length=150, default='ПК')
    model = models.CharField("Модель", max_length=100)
    form_factor = models.CharField("Форм-фактор корпуса", max_length=100, default='Mini-Tower')

# программное обеспечение
    OS = models.CharField("Операционная система", max_length=100, default='без ОС')

# процессор
    model_processor = models.CharField("Модель процессора", max_length=100, default='')
    core_processor = models.CharField("Кол-во ядер процессора", max_length=100, default='4')
    frequency_processor = models.CharField("Частота процессора", max_length=100, default='3600 МГц')

# видео карта
    type_videocard = models.CharField("Тип видео карты", max_length=100, default='встроенная')
    manufacture_chip = models.CharField("Производитель видеочипа", max_length=100, default='')
    model_videocard = models.CharField("Модель интегрированной видеокарты", max_length=100, default='')

# оперативная память
    type_RAM = models.CharField("Тип оперативноё памяти", max_length=100, default='DDR4')
    size_RAM = models.CharField("Размер оперативной памяти", max_length=100, default='8 ГБ')

# накопители данных
    HDD = models.CharField("Суммарный объем жестких дисков (HDD)", max_length=100, default='')
    SSD = models.CharField("Объем твердотельного накопителя (SSD)", max_length=100, default='4 ГБ')

# интерфейсы/разъёмы
    video_interface = models.CharField("Видео интерфейсы", max_length=100, default='')
    interface_periphery = models.CharField("Интерфейсы переферии", max_length=100, default='')

# габариты
    height = models.CharField("Длина", max_length=100, default='380 мм')
    width = models.CharField('Ширина', max_length=100, default='175 мм')
    depth = models.CharField('Высота', max_length=100, default='350 мм')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Системный блок'
        verbose_name_plural = 'Системные блоки'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('system_unit_product_url', kwargs={'url': self.url, 'category': self.category})


class Server(models.Model):
    category = models.CharField('имя модели', max_length=250, default='server')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна производитель', max_length=200)

# общие параметры
    type = models.CharField('Тип устройства', max_length=150, default='сервер')
    model = models.CharField("Модель", max_length=100)

# платформа
    form_factor = models.CharField("Форм-фактор сервера", max_length=100, default='')
    processor_socket = models.CharField("Процессорные сокеты", max_length=100, default='LGA1151')
    max_sum_RAM = models.CharField("Мак возможный суммарный объём ОЗУ", max_length=100, default='64 ГБ')
    storage_interface = models.CharField("Интерфейс накопителей", max_length=100, default='SATA')

# центральный процессор
    manufacture_processor = models.CharField("Производитель процессоров", max_length=100, default='Intel')
    model_processor = models.CharField("Модель процессоров", max_length=100, default='')
    base_frequency = models.CharField("Базовая частота", max_length=100, default='3500 МГц')

# подсистема памяти (ОЗУ)
    type_RAM = models.CharField("Тип оперативной памяти", max_length=100, default='DDR4 DIMM ECC')
    volume_RAM = models.CharField("Объём установленной оперативной памяти", max_length=100, default='8 ГБ')
    frequency_RAM = models.CharField("Частота оперативной памяти", max_length=100, default='3500 МГц')

# хранилище данных
    type_installed_drives = models.CharField("Тип установленных накопителей", max_length=100, default='HDD')
    storage_capacity = models.CharField("Объём установленных накопителей", max_length=100, default='1 ТБ')

# габариты
    width = models.CharField('Ширина', max_length=100, default='175 мм')
    height = models.CharField("Высота", max_length=100, default='359 мм')
    depth = models.CharField('Глубина', max_length=100, default='335 мм')
    massa = models.CharField("Вес", max_length=100, default='5 кг')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Сервер'
        verbose_name_plural = 'Сервер'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('server_product_url', kwargs={'url': self.url, 'category': self.category})


class Processor(models.Model):
    category = models.CharField('имя модели', max_length=250, default='processor')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='36 мес.')
    country = models.CharField('Страна производитель', max_length=200)

# общие параметры
    type = models.CharField('Тип устройства', max_length=150, default='процессор')
    model = models.CharField("Модель", max_length=100)
    generation_processor = models.CharField("Поколение процессоров", max_length=100, default='')
    code = models.CharField("Код производителя", max_length=100)
    year = models.CharField("Год релиза", max_length=100, default='')
    socket = models.CharField("Сокет", max_length=100, default='')

# ядро и архитектура
    core = models.CharField("Ядро", max_length=100, default='')
    number_core = models.CharField("Кол-во ядер", max_length=100, default='2')
    max_thread = models.CharField("Мак число потоков", max_length=100, default='2 шт')

# Частота
    frequency_processor = models.CharField("Базовая частота процессора (МГц)", max_length=100, default='3700 МГц')

# Параметры оперативной памяти
    type_memory = models.CharField("Тип памяти", max_length=100, default='DDR4')
    max_volume_memory = models.CharField("Мак поддерживаемый объём памяти", max_length=100, default='32 ГБ')
    min_frequency_RAM = models.CharField("Мин частота оперативной памяти", max_length=100, default='1333 МГц')
    max_frequency_RAM = models.CharField("Мак частота оперативной памяти", max_length=100, default='1333 МГц')

# тепловые хар-ки
    TDP = models.CharField("Тепловыделение(TDP)", max_length=100, default='25 Вт')
    max_temperature = models.CharField("Мак температура процессора", max_length=100, default='90 °C')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессор'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('processor_product_url', kwargs={'url': self.url, 'category': self.category})


class Motherboard(models.Model):
    category = models.CharField('имя модели', max_length=250, default='motherboard')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='36 мес.')
    country = models.CharField('Страна производитель', max_length=200, default='Китай')

# общие параметры
    type = models.CharField('Тип устройства', max_length=150, default='материнская плата')
    model = models.CharField("Модель", max_length=100)
    year = models.CharField("Год релиза", max_length=100, default='')
    form_factor = models.CharField("Форм-фактор", max_length=100, default='')
    socket = models.CharField("Сокет", max_length=100, default='')
    chipset = models.CharField("Чипсет", max_length=100, default='')

# память
    type_memory = models.CharField("Тип поддерживаемой памяти", max_length=100, default='DDR4')
    slot_memory = models.CharField("Кол-во слотов памяти", max_length=100, default='2')
    volume_memory = models.CharField("Мак объём памяти", max_length=100, default='32 ГБ')

# слоты расширения
    PCI_Express = models.CharField("Версия PCI Express", max_length=100, default='3.0')
    slot_PCI = models.CharField("Кол-во слотов PCI", max_length=100, default='нет')

# аудио
    sound = models.CharField("Звук", max_length=100, default='')
    chipset_sound = models.CharField("Чипсет звукового адаптера", max_length=100, default='')

# сеть
    network_adapter_chipset = models.CharField("Чипсет сетевого адаптера", max_length=100, default='')
    speed_network_adapter = models.CharField("Скорость сетевого адаптера", max_length=100, default='1000 Мбит/с')

# питание
    main_power_connector = models.CharField("Основной разъём питания", max_length=100, default='24-pin')
    processor_power_connector = models.CharField("Разъём питания процессора", max_length=100, default='4-pin')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Материнская плата'
        verbose_name_plural = 'Материнская плата'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('motherboard_product_url', kwargs={'url': self.url, 'category': self.category})


class VideoCard(models.Model):
    category = models.CharField('имя модели', max_length=250, default='videocard')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='36 мес.')
    country = models.CharField('Страна производитель', max_length=200, default='Китай')

# общие параметры
    type = models.CharField('Тип изделия', max_length=150, default='видеокарта')
    model = models.CharField("Модель", max_length=100, default='')
    year = models.CharField("Год релиза", max_length=100, default='')

# основные параметры
    range_graphic_processor = models.CharField("Линейка графических процессоров", max_length=100, default='')
    graphic_processor = models.CharField("Графический процессор", max_length=100, default='')

# Спецификация видеопроцессора
    videochip = models.CharField("Кол-во видеочипов", max_length=100, default='1')
    frequency_videochip = models.CharField("Штатная частота работы видеочипа(МГц)", max_length=100, default='954 МГц')
    temperature_processor = models.CharField("Мах температура процессора", max_length=100, default='95°')
    ray_tracing = models.CharField("Поддержка трассировки лучей", max_length=100, default='нет')

# спецификация видеопамяти
    volume_video_memory = models.CharField("Объём видеопамяти", max_length=100, default='1 ГБ')
    type_memory = models.CharField("Тип памяти", max_length=100, default='GDDR5')
    frequency_memory = models.CharField("Эффективная частота памяти(МГц)", max_length=100, default='5012 МГц')

# подключение
    interface_connection = models.CharField("Интерфейс подключения", max_length=100, default='PCI-E')
    PCI_Express = models.CharField("Версия PCI Express", max_length=100, default='3.0')

# питание
    max_power_consumption = models.CharField("Мак энергопотребление", max_length=100, default='19 Вт')
    power_supply = models.CharField("Рекомендуемый блок питания", max_length=100, default='300 Вт')

# габариты
    height = models.CharField("Длина видеокарты", max_length=100, default='140 мм')
    width = models.CharField("Толщина видеокарты", max_length=100, default='35 мм')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Видео карта'
        verbose_name_plural = 'Видео карта'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('videocard_product_url', kwargs={'url': self.url, 'category': self.category})


class RAMMemory(models.Model):
    category = models.CharField('имя модели', max_length=250, default='rammemory')
    url = models.SlugField('url', max_length=200, unique=True)
    image = models.ImageField('Изображение', upload_to='')
    price = models.PositiveIntegerField('Цена')
    description = models.TextField('Описание')

# заводские данные
    security = models.CharField('Гарантия', max_length=10, default='12 мес.')
    country = models.CharField('Страна производитель', max_length=200)

# классификация
    type = models.CharField('Тип устройства', max_length=150, default='оперативная память')
    model = models.CharField("Модель", max_length=100, default='')
    code = models.CharField("Код производителя", max_length=100, default='')
    year = models.CharField("Год релиза", max_length=100, default='')

# объём и состав комплекта
    type_memory = models.CharField("Тип памяти", max_length=100, default='DDR2')
    total_sum_memory = models.CharField("Объем одного модуля памяти ", max_length=100, default='2 ГБ')
    number_module = models.CharField("Кол-во модулей в комплекте", max_length=100, default='1 шт')

# быстродействие
    frequency = models.CharField("Тактовая частота", max_length=100, default='800 МГц')
    bandwidth = models.CharField("Пропускная способность", max_length=100, default='PC6400')

# тайминг
    cl = models.CharField("CAS Latency (CL)", max_length=100, default='')
    trcd = models.CharField("RAS to CAS Delay (tRCD)", max_length=100, default='')
    trp = models.CharField("Row Precharge Delay (tRP)", max_length=100, default='')
    tras = models.CharField("Activate to Precharge Delay (tRAS)", max_length=100, default='')

    shop = models.CharField('Наличие в магазине', max_length=150, default='есть')

    review = models.IntegerField('Кол-во отзывов', default=0)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Оперативная память'
        verbose_name_plural = 'Оперативная память'

    def get_absolute_url(self):
        self.category = self.__class__.__name__.lower()
        return reverse('rammemory_product_url', kwargs={'url': self.url, 'category': self.category})


def get_verbouse_field_name(self):
    return self._meta.get_field

def get_model_name(self):
    return self.__class__._meta.model_name

