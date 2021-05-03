from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *


User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ('email',)


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['name', 'text']

        widgets = {
            'text': forms.Textarea(attrs={'cols': 5, 'rows': 5}),
        }


class RegisterForm(UserCreationForm):

    email = forms.EmailField(max_length=150)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['first_name', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['first_name', 'email']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'buying_type', 'address']

        widgets = {
            'address': forms.Textarea(attrs={'cols': 30, 'rows': 2}),
            'buying_type': forms.RadioSelect()
        }


class FormMixin(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    CHOICES = (('есть', 'есть'), ('нет', 'нет'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
                                   label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
                                   label='Цена до ', required=False)  # max_value=20,

class DryMachineForm(FormMixin, forms.Form):

    MAX_LOAD = (('7 кг', '7 кг'), ('8 кг', '8 кг'), ('9 кг', '9 кг'), ('10 кг', '10 кг'))

    max_load = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Максимальная загрузка', required=False, choices=MAX_LOAD)

    heat_pump = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Тепловой насос', required=False, choices=FormMixin.CHOICES)

    block_child = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Блокировка от детей', required=False, choices=FormMixin.CHOICES)


class FridgeForm(FormMixin, forms.Form):
    COLD_STORAGE_SYSTEM = (('No Frost', 'No Frost'), ('капельная', 'капельная'))

    LOCATION_FREEZER_NTO = (('сверху', 'сверху'), ('слева', 'слева'), ('снизу', 'снизу'))

    cold_storage_system = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Система холодильного отделения', required=False, choices=COLD_STORAGE_SYSTEM)

    location_freezer_NTO = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Расположение морозильной камеры/НТО', required=False, choices=LOCATION_FREEZER_NTO)


class StoveForm(FormMixin, forms.Form):
    MATERIAL_COVER_PANEL = (('нержавеющая сталь', 'нержавеющая сталь'), ('стеклокерамика', 'стеклокерамика'),
                            ('эмалированная сталь', 'эмалированная сталь'))

    TOTAL_NUMBER_BURNETS = (('2 шт', '2 шт'), ('3 шт', '3 шт'), ('4 шт', '4 шт'))

    material_cover_panel = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Материал покрытия панели', required=False, choices=MATERIAL_COVER_PANEL)

    total_number_burnets = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Общие количество комфорок', required=False, choices=TOTAL_NUMBER_BURNETS)

    grill = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Гриль', required=False, choices=FormMixin.CHOICES)

    timer = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Таймер', required=False, choices=FormMixin.CHOICES)


class MicrowaveOvenForm(FormMixin, forms.Form):
    TYPE_MANAGEMENT = (('кнопки', 'кнопки'), ('поворотный механизм', 'поворотный механизм'),
                        ('сенсор', 'сенсор'))

    type_management = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Вид управления', required=False, choices=TYPE_MANAGEMENT)

    display = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Дисплей', required=False, choices=FormMixin.CHOICES)

    block_child = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Блокировка от детей', required=False, choices=FormMixin.CHOICES)


class KettleForm(FormMixin, forms.Form):
    BODY_MATERIAL = (('нержавеющая сталь', 'нержавеющая сталь'),
                     ('пластик', 'пластик'),
                     ('термостойкое стекло', 'термостойкое стекло'))

    body_material = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Материал корпуса', required=False, choices=BODY_MATERIAL)

    light = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Подсветка', required=False, choices=FormMixin.CHOICES)


class WashMachineForm(FormMixin, forms.Form):
    UPLOAD_TYPE = (('фронтальная', 'фронтальная'), ('вертикальная', 'вертикальная'))

    upload_type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Тип загрузки', required=False, choices=UPLOAD_TYPE)

    drive = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Прямой привод', required=False, choices=FormMixin.CHOICES)

    leak = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Защита от протечек', required=False, choices=FormMixin.CHOICES)


class IronForm(FormMixin, forms.Form):
    auto_shutdown = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Автоматическое отключение', required=False, choices=FormMixin.CHOICES)

    descaling_protection = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Система защиты от накипи', required=False, choices=FormMixin.CHOICES)


class HairdryerForm(FormMixin, forms.Form):
    IONIZATION = (('генератор ионов', 'генератор ионов'), ('нет', 'нет'), ('турмалиновая', 'турмалиновая'))

    cold_air_supply = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Подача холодного воздуха', required=False, choices=FormMixin.CHOICES)

    ionization = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Ионизация', required=False, choices=IONIZATION)


class HairClipperForm(FormMixin, forms.Form):
    TYPE_ENGINE = (('вибрационный', 'вибрационный'), ('роторный', 'роторный'))

    FOOD = (('от сети', 'от сети'),
            ('от сети/аккумулятора', 'от сети/аккумулятора'), ('от аккумулятора', 'от аккумулятора'))

    type_engine = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Тип двигателя', required=False, choices=TYPE_ENGINE)

    food = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Питание', required=False, choices=FOOD)


class SmartphoneForm(FormMixin, forms.Form):
    AMOUNT_RAM = (('16 Гб', '16 Гб'), ('32 Гб', '32 Гб'),
                  ('64 Гб', '64 Гб'), ('128 Гб', '128 Гб'), ('256 Гб', '256 Гб'), ('512 Гб', '512 Гб'))

    AMOUNT_INTERNAL_MEMORY = (('1 Гб', '1 Гб'), ('2 Гб', '2 Гб'),
                              ('3 Гб', '3 Гб'), ('4 Гб', '4 Гб'), ('6 Гб', '6 Гб'), ('8 Гб', '8 Гб'))

    amount_RAM = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Объём оперативной памяти', required=False, choices=AMOUNT_INTERNAL_MEMORY)

    amount_internal_memory = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Объём встроенной памяти', required=False, choices=AMOUNT_RAM)


class SmartWatchForm(FormMixin, forms.Form):
    sensor_display = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                       label='Сенсорный дисплей', choices=FormMixin.CHOICES, required=False)

    sim_cart = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                       label='Слот для SIM-карты', choices=FormMixin.CHOICES, required=False)


class TabletForm(FormMixin, forms.Form):
    screen_protection = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Защитное покрытие экрана', required=False, choices=FormMixin.CHOICES)

    front_camera = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Фронтальная камера', required=False, choices=FormMixin.CHOICES)


class EBookForm(FormMixin, forms.Form):
    display_sensor = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             label='Сенсорный дисплей', required=False, choices=FormMixin.CHOICES)

    SIM_cart = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             label='Слот для карты памяти', required=False, choices=FormMixin.CHOICES)


class TVForm(FormMixin, forms.Form):
    teletext = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         label='Телетекст', required=False, choices=FormMixin.CHOICES)

    subwoofer = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         label='Сабвуфер', required=False, choices=FormMixin.CHOICES)


class BracketTVForm(FormMixin, forms.Form):
    ADJUSTMENT = (('наклон', 'наклон'), ('наклон и поворот', 'наклон и поворот'), ('фиксированный', 'фиксированный'))

    adjustment = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          label='Угол наклона вверх', required=False, choices=ADJUSTMENT)


class ColumnForm(FormMixin, forms.Form):
    interface_USB = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          label='Интерфейс USB Type A', required=False, choices=FormMixin.CHOICES)


class HeadphonesForm(FormMixin, forms.Form):
    SHAPE = (('L-образная', 'L-образная'), ('прямая', 'прямая'), ('нет', 'нет'))

    microphone = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                              label='Микрофон', required=False, choices=FormMixin.CHOICES)

    shape_cable_plug = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                              label='Форма штекера кабеля', required=False, choices=SHAPE)


class NotebookForm(FormMixin, forms.Form):

    CONFIGURATION = (('только SSD', 'SSD'), ('один HDD + один SSD', 'HDD и SSD'))

    RAM = (('DDR4', 'DDR4'), ('LPDDR3', 'LPDDR3'), ('LPDDR4x', 'LPDDR4x'))

    storage_configuration = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                 label='Конфигурация накопителей', required=False, choices=CONFIGURATION)

    type_RAM = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                 label='Тип оперативной памяти', required=False, choices=RAM)


class SystemUnitForm(FormMixin, forms.Form):

    SISTEM = (('Windows 10 Домашняя', 'Windows 10 Домашняя'), ('Windows 10 Pro', 'Windows 10 Pro'),
              ('без ОС', 'без ОС'), ('Linux', 'Linux'))
    RAM = (('DDR4', 'DDR4'), ('DDR3', 'DDR3'))

    OS = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         label='Операционная система', required=False, choices=SISTEM)

    type_RAM = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         label='Тип оперативной памяти', required=False, choices=RAM)


class ServerForm(FormMixin, forms.Form):

    DRIVERS = (('нет', 'нет'), ('HDD', 'HDD'))

    type_installed_drives = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         label='Тип установленных накопителей', required=False, choices=DRIVERS)


class ProcessorForm(FormMixin, forms.Form):
    RAM = (('DDR4', 'DDR4'), ('DDR3', 'DDR3'))
    MEMORY = (('32 ГБ', '32 ГБ'), ('64 ГБ', '64 ГБ'), ('128 ГБ', '128 ГБ'), ('256 ГБ', '256 ГБ'))

    type_memory = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         label='Тип памяти', required=False, choices=RAM)

    max_volume_memory = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         label='Мак поддерживаемый объём памяти', required=False, choices=MEMORY)


class MotherboardForm(FormMixin, forms.Form):
    RAM = (('DDR4', 'DDR4'), ('DDR3', 'DDR3'))
    MEMORY = (('16 ГБ', '16 ГБ'), ('32 ГБ', '32 ГБ'), ('64 ГБ', '64 ГБ'), ('128 ГБ', '128 ГБ'))

    type_memory = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            label='Тип памяти', required=False, choices=RAM)

    volume_memory = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                  label='Мак объём памяти', required=False,
                                                  choices=MEMORY)


class VideoCardForm(FormMixin, forms.Form):

    RAM = (('GDDR5', 'GDDR5'), ('GDDR6', 'GDDR6'), ('GDDR6X', 'GDDR6X'))
    PROCESSOR = (('GeForce', 'GeForce'), ('Radeon', 'Radeon'))

    type_memory = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            label='Тип памяти', required=False, choices=RAM)

    range_graphic_processor = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                            label='Линейка графических процессоров', required=False, choices=PROCESSOR)


class RAMMemoryForm(FormMixin, forms.Form):

    RAM = (('DDR2', 'DDR2'), ('DDR3', 'DDR3'), ('DDR4', 'DDR4'))
    MODULE = (('1 шт', '1 шт'), ('2 шт', '2 шт'), ('4 шт', '4 шт'))

    type_memory = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            label='Тип памяти', required=False, choices=RAM)

    number_module = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                            label='Количество модулей в комплекте', required=False, choices=MODULE)
