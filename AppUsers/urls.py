from django.urls import path
from AppUsers.views import *  

urlpatterns = [
    #CRUD Usuario
    path('', leerUsuarios, name="leerUsuarios"),
    path('editarUsuario/<id>', editarUsuario, name="editarUsuario"),
    path('eliminarUsuario/<id>', eliminarUsuario, name="eliminarUsuario"),

    ]