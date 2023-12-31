from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User

from post.models import Post


def homepage(request):
    posts = Post.objects.all().order_by('created_at')[:4]

    return render(request, 'core/homepage.html',{
        'posts': posts,
    })

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        print(password)

        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            # password=password,
        )
        user.set_password(password)
        user.save()

        return redirect('/login/')

    return render(request, 'core/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/myaccount/')
        else:
            return render(request, 'core/login.html')
    else:
        return render(request, 'core/login.html')

def myaccount(request):
    posts = Post.objects.filter(author = request.user).order_by('-created_at')

    return render(request, 'core/myaccount.html', {
        'posts': posts,
    })

def edit_account(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')

        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.email = email
        
        request.user.save()

        return redirect('/myaccount/')

    return render(request, 'core/edit_account.html')


@login_required
def my_post(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')

    return render(request, 'core/my_post.html', { 
        'posts': posts,
    })