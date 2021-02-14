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


class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'image')
    list_filter = ('title', 'image',)
    # list_display_links = ('url',)
    search_fields = ('title',)
    save_on_top = True

admin.site.register(Fridge)
admin.site.register(Stove)
admin.site.register(MicrowaveOven)


# class Kettle(admin.ModelAdmin):
#     list_display = ('model',)
#     list_filter = ('model', )

admin.site.register(Kettle)

admin.site.register(Iron)
admin.site.register(WashMachine)
admin.site.register(DryMachine)
admin.site.register(Hairdryer)
admin.site.register(HairClipper)
admin.site.register(Smartphone)
admin.site.register(SmartWatch)
admin.site.register(Tablet)
admin.site.register(EBook)
admin.site.register(TV)
admin.site.register(BracketTV)
admin.site.register(Column)
admin.site.register(Headphones)
admin.site.register(Notebook)
admin.site.register(SystemUnit)
admin.site.register(Server)
admin.site.register(Processor)
admin.site.register(Motherboard)
admin.site.register(VideoCard)
admin.site.register(RAMMemory)

# class DryMachineAdmin(admin.ModelAdmin):
#     list_display = ('title', 'url', 'image')
#     save_on_top = True

admin.site.register(Review)
admin.site.register(MainMenu)
admin.site.register(Menu)
admin.site.register(SubMenu)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(CartProduct)



# from mptt.admin import MPTTModelAdmin
#
# admin.site.register(MainM, MPTTModelAdmin)





