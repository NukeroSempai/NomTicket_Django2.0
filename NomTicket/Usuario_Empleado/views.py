from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import empleadoForm, loginEmpForm
from CORE.models import EMPLEADO, PRODUCTO, TICKET
from django.contrib import messages
from datetime import date
from datetime import datetime

#v_global
g_rut_emp = ""

def inicio(request):
    return render(request, 'inicio.html')


def logout(request):
    return redirect("/")


def login_empleado(request):
    if request.method == 'POST':
        form = loginEmpForm(request.POST)
        if form.is_valid:
            global g_rut_emp
            g_rut_emp = request.POST['rut_emp']
            clave = request.POST['clave']
            empleados = EMPLEADO.objects.filter(rut_emp = g_rut_emp)
            data = {
                'empleados' : empleados
            }
            for empleado in empleados:
                clave_emp=empleado.clave
                print("nom_emp",g_rut_emp)
                print("clave",clave)
                print ("clave_emp",clave_emp)
            if (clave == clave_emp):
                print("si")
            #verificar = EMPLEADO.objects.filter(rut_emp=g_rut_emp, clave=clave).exists()
            #if verificar == True:
                today = date.today()
                now = datetime.now()
                formato = now.strftime('%d/%m/%Y-%H:%M:%S')
                messages.info(request, f'FECHA: {formato}')
                empleados = EMPLEADO.objects.filter(rut_emp=g_rut_emp)
                data = {
                    'empleados': empleados
                }
                print("primero")
                return render(request, "home_empleado.html", data)
            else:
                print("segundo")
                messages.error(
                    request, 'Por favor, introduzca un nombre de usuario y clave correctos.Observe que ambos campos pueden ser sensibles a mayúsculas.')
                return redirect('/login_empleado')
    else:
        form = loginEmpForm
        print("tercero")
        return render(request, "login_empleado.html", {'form': form})


def prueba(request):
    global g_rut_emp
    print(g_rut_emp)
    empleados = EMPLEADO.objects.filter(rut_emp=g_rut_emp)
    data = {
        'empleados': empleados
    }
    return render(request, "prueba.html", data)


def home_empleado(request):
    productos = PRODUCTO.objects.all()
    context = {'productos' : productos}
    return render(request, 'home_empleado.html', context)

def carrito_empleado(request):
    context = {}
    return render(request, 'carrito_empleado.html', context)

def emitir_ticket_empleado(request):
    context = {}
    return render(request, 'emitir_ticket_empleado.html', context)


#@login_required(login_url='home')
def lista_productos(request):
    global g_rut_emp
    if g_rut_emp !=" ":
        print(g_rut_emp)
    empleados = EMPLEADO.objects.filter(rut_emp=g_rut_emp)
    data = {
        'empleados': empleados
    }
    productos = PRODUCTO.objects.all().order_by('codigo_producto')
    if productos!="":
        producto = PRODUCTO.objects.get(codigo_producto=1)
        print(producto)
    context =  {'empleados': empleados , 'productos' : productos}
    return render(request, 'lista_productos.html',context)
    
    
