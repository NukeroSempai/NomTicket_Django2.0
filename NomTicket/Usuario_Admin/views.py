from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import empleadoForm, loginEmpForm
from CORE.models import EMPLEADO
from django.contrib import messages
from datetime import date
from datetime import datetime

def inicio(request):
    return render(request, 'inicio.html')

def lista_empleado(request):
    empleados =  EMPLEADO.objects.all()
    #empleados =  EMPLEADO.objects.filter(nom_emp = 'juan')
    data = {
        'empleados' : empleados
    }
    return render(request,"lista_empleado.html", data)

def form_empleado(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = empleadoForm()
        else:
            empleado = EMPLEADO.objects.get(pk=id)
            form = empleadoForm(instance=empleado)
        return render(request,"form_empleado.html",{'form':form})
    else:
        if id == 0:
            form = empleadoForm(request.POST)
        else:
            empleado = EMPLEADO.objects.get(pk=id)
            form = empleadoForm(request.POST,instance= empleado)
        if form.is_valid():
            form.save()
        return redirect('/lista')
               
def eliminar_empleado(request,id):
    Empleado = EMPLEADO.objects.get(pk=id)
    Empleado.delete()
    return redirect('/lista')

def logout(request): 
    return redirect("/")

def home_admin(request):
    return render(request,"home_admin.html")
