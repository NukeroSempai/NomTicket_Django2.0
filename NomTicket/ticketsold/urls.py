from django.urls import path
from . import views

urlpatterns = [
    path('lista_productos', views.empleado, name="lista_productos"),
    path('tickets_emitidos/', views.tickets_emitidos, name="tickets_emitidos"),
    path('ticket_empleado/', views.ticket_empleado, name="ticket_empleado"),
]