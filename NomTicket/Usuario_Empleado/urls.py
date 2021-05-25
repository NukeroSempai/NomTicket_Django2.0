"""NomTicket URL Configuration

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
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.inicio,name="inicio"),
    path('home_empleado/', views.home_empleado, name="home_empleado"),
    path('login_empleado/', views.login_empleado, name="login_empleado"),
    path('carrito_empleado/', views.carrito_empleado, name="carrito_empleado"),
    path('emitir_ticket_empleado', views.emitir_ticket_empleado, name="emitir_ticket_empleado"),
    path('logout/', views.logout, name="logout"),
    path('prueba/', views.prueba, name="prueba" ),
    path('lista_productos/', views.lista_productos, name="lista_productos"),
    
]