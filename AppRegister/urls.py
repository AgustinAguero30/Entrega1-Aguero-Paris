from django.urls import path, include
from AppRegister.views import *
from AppTienda.views import *


urlpatterns = [
    # Registrar
    path('register/', register, name='register'),
    # Editar Usuario
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
]