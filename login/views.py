from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def django_login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username = email, pwd = password)
        if user is not None:
            #Logs in User
            login(request.user)
            # directs him to courseInfo page
            return redirect('courseInfo')
    return render(request, 'login/login.html')

def django_logout(request):
    logout(request)
     # directs him to home page
    return redirect('home')