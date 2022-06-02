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

def doLogin(request):
     
    print("here")
    email_id = request.GET.get('email')
    password = request.GET.get('password')
    # user_type = request.GET.get('user_type')
    print(email_id)
    print(password)
    print(request.user)
    if not (email_id and password):
        messages.error(request, "Please provide all the details!!")
        return render(request, 'login_page.html')
 
    user = CustomUser.objects.filter(email=email_id, password=password).last()
    if not user:
        messages.error(request, 'Invalid Login Credentials!!')
        return render(request, 'login_page.html')
 
    login(request, user)
    print(request.user)
 
    if user.user_type == CustomUser.STUDENT:
        return redirect('student_home/')
    elif user.user_type == CustomUser.STAFF:
        return redirect('staff_home/')
    elif user.user_type == CustomUser.HOD:
        return redirect('admin_home/')
 
    return render(request, 'home.html')