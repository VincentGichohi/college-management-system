
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect

class LoginCheckMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
