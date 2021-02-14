from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import * # CustomUser, Review, Order


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


class DryMachineForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))
    MAX_LOAD = (('7 кг', '7 кг'), ('8 кг', '8 кг'), ('9 кг', '9 кг'), ('10 кг', '10 кг'))
    CHOICES = (('есть', 'есть'), ('нет', 'нет'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,

    max_load = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Максимальная загрузка', required=False, choices=MAX_LOAD)

    heat_pump = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Тепловой насос', required=False, choices=CHOICES)

    block_child = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Блокировка от детей', required=False, choices=CHOICES)


class FridgeForm(forms.Form):
    COLD_STORAGE_SYSTEM = (('No Frost', 'No Frost'), ('капельная', 'капельная'))

    LOCATION_FREEZER_NTO = (('сверху', 'сверху'), ('слева', 'слева'), ('снизу', 'снизу'))

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,

    cold_storage_system = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Система холодильного отделения', required=False, choices=COLD_STORAGE_SYSTEM)

    location_freezer_NTO = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Расположение морозильной камеры/НТО', required=False, choices=LOCATION_FREEZER_NTO)


class StoveForm(forms.Form):
    MATERIAL_COVER_PANEL = (('нержавеющая сталь', 'нержавеющая сталь'), ('стеклокерамика', 'стеклокерамика'),
                            ('эмалированная сталь', 'эмалированная сталь'))

    TOTAL_NUMBER_BURNETS = (('2 шт', '2 шт'), ('3 шт', '3 шт'), ('4 шт', '4 шт'))

    CHOICES = (('есть', 'есть'), ('нет', 'нет'))

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,

    material_cover_panel = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Материал покрытия панели', required=False, choices=MATERIAL_COVER_PANEL)

    total_number_burnets = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Общие количество комфорок', required=False, choices=TOTAL_NUMBER_BURNETS)

    grill = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Гриль', required=False, choices=CHOICES)

    timer = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Таймер', required=False, choices=CHOICES)


class MicrowaveOvenForm(forms.Form):
    TYPE_MANAGEMENT = (('кнопки', 'кнопки'), ('поворотный механизм', 'поворотный механизм'),
                            ('сенсор', 'сенсор'))

    CHOICES = (('есть', 'есть'), ('нет', 'нет'))

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,

    type_management = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Вид управления', required=False, choices=TYPE_MANAGEMENT)

    display = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Дисплей', required=False, choices=CHOICES)

    block_child = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Блокировка от детей', required=False, choices=CHOICES)


class KettleForm(forms.Form):
    BODY_MATERIAL = (('нержавеющая сталь', 'нержавеющая сталь'), ('пластик', 'пластик'), ('термостойкое стекло', 'термостойкое стекло'))

    CHOICES = (('есть', 'есть'), ('нет', 'нет'))

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,

    body_material = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Материал корпуса', required=False, choices=BODY_MATERIAL)

    light = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Подсветка', required=False, choices=CHOICES)


class WashMachineForm(forms.Form):
    UPLOAD_TYPE = (('фронтальная', 'фронтальная'), ('вертикальная', 'вертикальная'))

    CHOICES = (('есть', 'есть'), ('нет', 'нет'))

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,

    upload_type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Тип загрузки', required=False, choices=UPLOAD_TYPE)

    drive = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Прямой привод', required=False, choices=CHOICES)

    leak = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Защита от протечек', required=False, choices=CHOICES)


class IronForm(forms.Form):
    CHOICES = (('есть', 'есть'), ('нет', 'нет'))

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
                                   label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
                                   label='Цена до ', required=False)  # max_value=20,

    auto_shutdown = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Автоматическое отключение', required=False, choices=CHOICES)

    descaling_protection = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Система защиты от накипи', required=False, choices=CHOICES)


class HairdryerForm(forms.Form):
    IONIZATION = (('генератор ионов', 'генератор ионов'), ('нет', 'нет'), ('турмалиновая', 'турмалиновая'))

    CHOICES = (('есть', 'есть'), ('нет', 'нет'))

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,

    cold_air_supply = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Подача холодного воздуха', required=False, choices=CHOICES)

    ionization = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Ионизация', required=False, choices=IONIZATION)


class HairClipperForm(forms.Form):
    TYPE_ENGINE = (('вибрационный', 'вибрационный'), ('роторный', 'роторный'))

    FOOD = (('от сети', 'от сети'), ('от сети/аккумулятора', 'от сети/аккумулятора'), ('от аккумулятора', 'от аккумулятора'))

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,

    type_engine = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Тип двигателя', required=False, choices=TYPE_ENGINE)

    food = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Тип двигателя', required=False, choices=FOOD)


class SmartphoneForm(forms.Form):
    AMOUNT_RAM = (('16 Гб', '16 Гб'), ('32 Гб', '32 Гб'),
                              ('64 Гб', '64 Гб'), ('128 Гб', '128 Гб'), ('256 Гб', '256 Гб'), ('512 Гб', '512 Гб'))

    AMOUNT_INTERNAL_MEMORY = (('1 Гб', '1 Гб'), ('2 Гб', '2 Гб'),
                  ('3 Гб', '3 Гб'), ('4 Гб', '4 Гб'), ('6 Гб', '6 Гб'), ('8 Гб', '8 Гб'))

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,

    amount_RAM = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Объём оперативной памяти', required=False, choices=AMOUNT_INTERNAL_MEMORY)

    amount_internal_memory = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        label='Объём встроенной памяти', required=False, choices=AMOUNT_RAM)


class SmartWatchForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,


class TabletForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,

    # amount_RAM = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
    #     label='Тип двигателя', required=False, choices=FOOD)
    #
    # amount_internal_memory = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
    #     label='Тип двигателя', required=False, choices=FOOD)


class EBookForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,


class TVForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,


class BracketTVForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,


class ColumnForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,


class HeadphonesForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,


class NotebookForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,


class SystemUnitForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,


class ServerForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,


class ProcessorForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,



class MotherboardForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,



class VideoCardForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,



class RAMMemoryForm(forms.Form):

    ORDERING = (('model', 'умолчанию'), ('price', 'возростанию цены'), ('-price', 'убыванию цены'))

    ordering = forms.ChoiceField(label='Сортировать по:', choices=ORDERING, required=False)

    min_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена от ', required=False)  # min_value=20,

    max_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '0'}),
        label='Цена до ', required=False)  # max_value=20,


