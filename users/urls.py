from django.urls import path
from . import views
from users.views import export, export_data, export_records, export_user_blogs,get_user_info, profile

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('info/<str:username>/', views.get_user_info, name='user_info'),
    path('profile/', views.profile, name='profile'),
    
    path('export/', views.export, name='export'),
    path('export-data/', views.export_data, name='export_data'),
    path('export-records/', views.export_records, name='export_records'),
    path('export-user-blogs/', views.export_user_blogs, name='export_user_blogs'),
]
