
import json
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.csrf import csrf_exempt

from .EmailBackend import EmailBackend
from .models import Session, Attendance, Subject

def login_page(request):
    if request.user.is_authenticated:
        if request.user_type == '1':
            return redirect(reverse("admin_home"))
        elif request.user_type == '2':
            return redirect(reverse("staff_home"))
        else:
            return redirect(reverse("student_home"))
    return render(request, 'student_management_app/login.html')

