
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class UserModel(UserAdmin):
    ordering = ('email',)
