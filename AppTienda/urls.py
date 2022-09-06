from django.urls import path
from AppTienda.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('clientes/', clientes, name="clientes"),
    path('zapatillas/', zapatillas, name="zapatillas"),
    path('remeras/', remeras, name="remeras"),
    path('pantalones/', pantalones, name="pantalones"),
    path('busquedaClientes/', busquedaClientes, name="busquedaClientes"),
    path('buscar/', buscar, name="buscar"),
]