from django.urls import path

from . import views


app_name = 'post'

urlpatterns = [
    path('detail/<slug:slug>/', views.detail, name='detail'),
    path('tags-post/<int:pk>/', views.tag_post, name='tag_post'),
    path('new/', views.new, name='new'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    
]
