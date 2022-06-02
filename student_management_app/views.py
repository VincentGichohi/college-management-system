from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser, Staffs, Students, AdminHOD
from django.contrib import messages

def home(request):
    return render(request, 'home.html')
 
def contact(request):
    return render(request, 'contact.html')
 
def loginUser(request):
    return render(request, 'login_page.html')