from django.urls import path
from AppRegister.views import *


urlpatterns = [
    # Registrar
    path('', register, name='register'),
    # Editar Usuario
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
]