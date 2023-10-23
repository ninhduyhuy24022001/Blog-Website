from django.shortcuts import render, redirect
from .models import User


def homepage(request):

    return render(request, 'core/homepage.html')

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )

        return redirect('/login/')

    return render(request, 'core/signup.html')

def login(request):
    
    return render(request, 'core/login.html')