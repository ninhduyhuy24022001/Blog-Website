from django.urls import path

from . import views


app_name = 'post'

urlpatterns = [
    path('<slug:slug>/', views.detail, name='detail')
]
