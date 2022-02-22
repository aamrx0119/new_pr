from django.contrib import admin
from django import forms
from .forms import UserChangeForm,UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import MyUser


# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    
    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','bio')}),
        ('Permissions', {'fields': ('is_admin','is_active')}),
    )
    

    add_fieldsets = (
        ('Add new user', {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name', 'bio','password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email','is_admin')
    filter_horizontal = ()



admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)
