from django.urls import path
from AppTienda.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('zapatillas/', zapatillas, name="zapatillas"),

    path('busquedaZapatillas/', busquedaZapatillas, name="busquedaZapatillas"),

    path('buscarZapatilla/', buscarZapatilla, name="buscarZapatilla"),
    
    #CRUD Zapatillas
    path('leerZapatillas/', leerZapatillas, name="leerZapatillas"),
    path('editarZapatilla/<id>', editarZapatilla, name="editarZapatilla"),
    path('eliminarZapatilla/<id>', eliminarZapatilla, name="eliminarZapatilla"),
    path('infoZapatilla/<id>', infoZapatilla, name="infoZapatilla"),

    #Agregar Avatar
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
]