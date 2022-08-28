from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from student_management_app.models import *
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import *
# class UserModel(UserAdmin):
#     ordering = ('email',)


# admin.site.register(UserModel)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Session)





User = get_user_model()

# Remove Group Model from admin. We're not using it.
# admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserAdminChangeForm
    add_form = CustomUserForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email',]
    list_filter = []
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ()}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',)}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)