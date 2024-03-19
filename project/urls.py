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

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", views.index_view, name='index'),
    
#     path("", views.home, name="home"),
#     path("login/", views.login, name="login"),
#     path("register/", views.register, name="register"),
#     path("new_car_registration/", views.new_car_registration_view, name="new_car_registration")
# ]

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    # Define the path for the root URL to render index.html as the home page
    path("", TemplateView.as_view(template_name='index.html'), name='home'),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path('base.html/', TemplateView.as_view(template_name='base.html'), name='base'),
    path("new_car_registration/", views.new_car_registration_view, name="new_car_registration"),

]








