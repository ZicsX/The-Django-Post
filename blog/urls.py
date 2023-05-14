from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.blog_new, name='blog_new'),
    path('edit/<int:blog_id>/', views.blog_edit, name='blog_edit'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('delete/<int:blog_id>/', views.blog_delete, name='blog_delete'),
    path('', views.home, name='home'),
]
