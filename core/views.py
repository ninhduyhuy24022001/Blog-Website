from django.shortcuts import render


def homepage(request):

    return render(request, 'core/homepage.html')

def signup(request):
    
    return render(request, 'core/signup.html')

def login(request):
    
    return render(request, 'core/login.html')