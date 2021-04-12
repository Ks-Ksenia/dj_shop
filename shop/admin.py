from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User

from .forms import UserCreationForm, UserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name')

admin.site.register(CustomUser, CustomUserAdmin)


class AdminProductMixin(admin.ModelAdmin):
    list_display = ('model', 'price', 'shop')
    list_filter = ('shop', 'price')
    search_fields = ('model', 'price')
    ordering = ('model', 'price')
    prepopulated_fields = {'url': ('type', 'model')}
    save_on_top = True
    show_full_result_count = True

admin.site.register(Fridge, AdminProductMixin)
admin.site.register(Stove, AdminProductMixin)
admin.site.register(MicrowaveOven, AdminProductMixin)
admin.site.register(Kettle, AdminProductMixin)
admin.site.register(Iron, AdminProductMixin)
admin.site.register(WashMachine, AdminProductMixin)
admin.site.register(DryMachine, AdminProductMixin)
admin.site.register(Hairdryer, AdminProductMixin)
admin.site.register(HairClipper, AdminProductMixin)
admin.site.register(Smartphone, AdminProductMixin)
admin.site.register(SmartWatch, AdminProductMixin)
admin.site.register(Tablet, AdminProductMixin)
admin.site.register(EBook, AdminProductMixin)
admin.site.register(TV, AdminProductMixin)
admin.site.register(BracketTV, AdminProductMixin)
admin.site.register(Column, AdminProductMixin)
admin.site.register(Headphones, AdminProductMixin)
admin.site.register(Notebook, AdminProductMixin)
admin.site.register(SystemUnit, AdminProductMixin)
admin.site.register(Server, AdminProductMixin)
admin.site.register(Processor, AdminProductMixin)
admin.site.register(Motherboard, AdminProductMixin)

admin.site.register(VideoCard, AdminProductMixin)
admin.site.register(RAMMemory, AdminProductMixin)

admin.site.register(Review)
admin.site.register(MainMenu)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'category')
    prepopulated_fields = {'url': ('title',)}

admin.site.register(Menu, MenuAdmin)
admin.site.register(SubMenu, MenuAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer')
admin.site.register(Cart, CartAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'last_name',)
    ordering = ('last_name',)
    search_fields = ('number', 'last_name',)
admin.site.register(Order, OrderAdmin)


admin.site.register(CartProduct)
admin.site.register(Customer)







