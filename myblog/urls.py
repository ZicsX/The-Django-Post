from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from users.views import UserViewSet
from django.contrib.auth import views as auth_views
from blog import views as blog_views

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('blog/', include('blog.urls')),
    # path('api/', include(router.urls)),
    path('', blog_views.home, name='home'),
]
