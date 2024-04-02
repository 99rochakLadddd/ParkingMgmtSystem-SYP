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
from django.urls import path, include
from app import views
from django.views.generic import TemplateView
# from .views import new_car_registration_view

urlpatterns = [
    path("admin/", admin.site.urls),
    # Define the path for the root URL to render index.html as the home page
    path("", TemplateView.as_view(template_name='login.html'), name='login'),
    path("login/", views.login_view, name="login"),
    path("index/", views.index_view, name="index"),
    path("register/", views.register_view, name="register"),
    path('logout/', views.logout_view, name='logout'),
    path('base.html/', TemplateView.as_view(template_name='base.html'), name='base'),
    path("new_car_registration/", views.new_car_registration_view, name="new_car_registration"),
    path("manage_user.html/", views.manage_user_view, name="manage_user"),
    path('admin/', views.admin_view, name='admin_view'),
    # path('create/', views.new_car_registration_view,name="new_car_registration")
]








