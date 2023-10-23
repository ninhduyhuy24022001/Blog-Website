from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


app_name = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
