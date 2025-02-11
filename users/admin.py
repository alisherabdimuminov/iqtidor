from django.contrib import admin
from unfold import admin as unfold_admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


@admin.register(User)
class UserModelAdmin(UserAdmin, unfold_admin.ModelAdmin):
    add_form = UserCreationForm
    form_class=  UserChangeForm
    list_display = ["username", "first_name", "last_name", "middle_name",]
    add_fieldsets = (
        ("Yangi foydalanuvchi qo'shish", {
            "fields": ("username", "first_name", "last_name", "middle_name", "city", "town", "rural", "school", "image", "is_student", "is_active", )
        })
    )
    fieldsets = (
        ("Foydalanuvchi", {
            "fields": ("username", "first_name", "last_name", "middle_name", "city", "town", "rural", "school", "image", "is_student", "is_active", )
        }),
    )