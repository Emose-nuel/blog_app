from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','first_name', 'username', 'is_staff', ] # new
    fieldsets = UserAdmin.fieldsets #+ (  (None, {'fields': ('age',)}),)

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email','first_name',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
