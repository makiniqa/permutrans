"""trueque URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from accounts.views import register_page, login_page, logout_user
from pages.views import home_page, profile_page
from items.views import item_create, item_all, item_detail, item_delete, item_update

urlpatterns = [
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('registrarse', register_page, name='register'),
    path('iniciar', login_page, name='login'),
    path('salir', logout_user, name='logout'),
    path('perfil', profile_page, name='profile'),
    path('subir', item_create, name='create'),
    path('placard', item_all, name='all'),
    path('prenda/<int:pk>', item_detail, name='item-detail'),
    path('delete/<int:item_id>', item_delete, name='delete'),
    path('update/<int:item_id>', item_update, name='update'),
]
