from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from CORE.models import EMPLEADO
from django.contrib import messages
from datetime import date
from datetime import datetime

def inicio(request):
    return render(request, 'inicio.html')

def home_visitante(request):
    return render(request,"home_visitante.html")

def login_visitante(request):   
    return render(request,"login_visitante.html")