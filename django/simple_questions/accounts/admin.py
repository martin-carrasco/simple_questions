from django.contrib import admin
from django.contrib.auth.admin import BaseUserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser
from .forms import UserCreationForm, UserChangeForm

class CustomUserAdmin(BaseUserAdmin):
    form = UserCreationForm
    add_form = UserChangeForm

    list_display = ('email', 'display_name', 'is_staff', 'username')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('display_name',)}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'display_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
