from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import empleadoForm, loginEmpForm
from CORE.models import EMPLEADO
from django.contrib import messages
from datetime import date
from datetime import datetime

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


def inicio(request):
    return render(request, 'inicio.html')

def logout(request): 
    return redirect("/")

def login_empleado(request):
    if request.method =='POST':
        form = loginEmpForm(request.POST) 
        if form.is_valid:
            rut_emp = request.POST['rut_emp']
            clave = request.POST['clave']            
            verificar = EMPLEADO.objects.filter(rut_emp= rut_emp, clave= clave).exists()            
            if verificar == True:   
                today = date.today()
                now = datetime.now()
                formato = now.strftime('%d/%m/%Y-%H:%M:%S')                
                messages.info(request, f'Fecha: {formato}')
                empleados =  EMPLEADO.objects.filter(rut_emp = rut_emp)
                data = {
                        'empleados' : empleados
                }
                print ("primero")
                return render(request,"home_empleado.html", data)               
            else:
                print ("segundo")
                messages.error(request,'Por favor, introduzca un nombre de usuario y clave correctos.Observe que ambos campos pueden ser sensibles a mayúsculas.')      
                return redirect('/login_empleado')  
    else:    
        form = loginEmpForm
        print ("tercero")
        return render(request,"login_empleado.html", {'form':form})


def home_empleado(request):
    return render(request,"home_empleado.html")

def login_visitante(request):   
    return render(request,"login_visitante.html")

def home_admin(request):
    return render(request,"home_admin.html")

def home_visitante(request):
    return render(request,"home_visitante.html")

def inicio(request):
    return render(request, 'inicio.html')

def tickets_emitidos(request):
    return render(request, 'lista_tickets_emitidos.html')

def empleado(request):
    return render(request, 'empleado.html')

def login_visitante(request):   
    return render(request,"login_visitante.html")

def visitante(request):
    return render(request, 'visitante.html')
