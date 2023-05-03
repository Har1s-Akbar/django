from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .usersforms import CustomUserChangeForm,CustomUserCreation

customUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreation
    form = CustomUserChangeForm
    model = customUser
    list_display = ['username','email']


admin.site.register(customUser, CustomUserAdmin)