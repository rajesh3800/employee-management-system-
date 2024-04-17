"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home,name='home'),
    path('all_emp',all_emp,name='all_emp'),
    path('add_emp',add_emp,name='add_emp'),
    path('remove_emp',remove_emp,name='remove_emp'),
    path('filter_emp',filter_emp,name="filter_emp"),
    path('update_emp',update_emp,name='update_emp'),
    path('register',register,name='register'),
    path('user_login',user_login,name='user_login'),
    path('logout', user_Logout, name='user_Logout'),
    path('forget_password', forget_password, name='forget_password'),
    path('verification', verification, name='verification'),
    path('password', password, name='password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
