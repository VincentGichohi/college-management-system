
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, AdminHOD, Staffs, Courses, Subjects, Students, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaffs, NotificationStudent, NotificationStaffs
from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminChangeForm, UserAdminCreationForm
# Register your models here.


User = get_user_model()
class UserModel(BaseUserAdmin):
    #The forms to add and change user instances.
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    #The fields to be used in displaying the User Model.
    #These override the definition on the base UserAdmin
    #that references specific fields on auth.user
    list_display = ['email', 'admin']
    list_filter = ['admin']
    fieldsets = (
        (None, {'felds': ('email', 'password')}),
        ('Personal Info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )
    #add fieldsets is not a standard ModelAdmin attribute. UserAdmin
    #overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('email', 'password1', 'password2')
        }),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()
 
 
admin.site.register(CustomUser, UserModel)
 
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Students)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)