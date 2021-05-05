from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from CORE.models import PRODUCTO, TICKET, EMPLEADO

# Create your views here.
#@login_required(login_url='')
def tickets_emitidos(request):
    tickets = TICKET.objects.all().order_by('fecha_imp')
    return render(request, 'lista_tickets_emitidos.html', {'tickets' : tickets })

#@login_required(login_url='')
def empleado(request):
    productos = PRODUCTO.objects.all().order_by('codigo_producto')
    #productos = PRODUCTO.objects.filter(codigo_producto=21)
    return render(request, 'empleado.html', {'productos' : productos })

#@login_required(login_url='')
def ticket_empleado(request):
    return render(request, 'ticket_empleado.html')