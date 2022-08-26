
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from student_management_app.models import *


class UserModel(UserAdmin):
    ordering = ('email',)


admin.site.register(CustomUser, UserModel)
