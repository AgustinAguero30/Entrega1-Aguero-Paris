from django.urls import path
from AppTienda.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('clientes/', clientes, name="clientes"),
    path('zapatillas/', zapatillas, name="zapatillas"),
    path('remeras/', remeras, name="remeras"),
    path('pantalones/', pantalones, name="pantalones"),

    path('busquedaClientes/', busquedaClientes, name="busquedaClientes"),
    path('busquedaZapatillas/', busquedaZapatillas, name="busquedaZapatillas"),
    path('busquedaPantalones/', busquedaPantalones, name="busquedaPantalones"),
    path('busquedaRemeras/', busquedaRemeras, name="busquedaRemeras"),

    path('buscarCliente/', buscarCliente, name="buscarCliente"),
    path('buscarZapatilla/', buscarZapatilla, name="buscarZapatilla"),
    path('buscarPantalon/', buscarPantalon, name="buscarPantalon"),
    path('buscarRemera/', buscarRemera, name="buscarRemera"),

    #CRUD Zapatillas
    path('leerZapatillas/', leerZapatillas, name="leerZapatillas"),
    path('editarZapatilla/<id>', editarZapatilla, name="editarZapatilla"),
    path('eliminarZapatilla/<id>', eliminarZapatilla, name="eliminarZapatilla"),
    path('infoZapatilla/<id>', infoZapatilla, name="infoZapatilla"),

    #Agregar Avatar
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
]