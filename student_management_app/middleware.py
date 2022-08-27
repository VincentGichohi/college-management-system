from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect


class LoginCheckMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user  # Check the current user
        if user.is_authenticated:
            if user.user_type == '1':  # Is it the HOD/Admin?
                if modulename == 'student_management_app.student_views':
                    return redirect(reverse('admin_home'))
            elif user.user_type == '2':  # Staff
                if modulename == 'student_management_app.student_views' or modulename == 'student_management_app' \
                                                                                         '.hod_views':
                    return redirect(reverse('student_home'))
            else:
                return redirect(reverse('login_page'))
        else:
            if request.path == reverse('login_page') or modulename == 'django.contrib.auth.views' or request.path == reverse('user_login'):  # If
                pass
            else:
                return redirect(reverse('login_page'))