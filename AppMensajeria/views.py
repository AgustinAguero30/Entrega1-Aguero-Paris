from django.shortcuts import render
from AppMensajeria.models import *
from AppMensajeria.forms import *
from django.contrib.auth.decorators import login_required
from AppUsers.forms import *
from AppTienda.views import obtenerAvatar

#Crear Mensaje

# def crearMensaje(request):
#     if request.method == "POST":      
#         form=Message(request.POST, request.FILES)
#         if form.is_valid():
#             informacion= form.cleaned_data
#             receptor=informacion["receptor"]
#             content=informacion["content"]
#             is_read=True
#             mensaje=Message(emisor= request.user, receptor=receptor,content=content,is_read=is_read)           
#             mensaje.save()
#             return render (request, "AppMensajeria/leerMensaje.html", {"mensaje" : "Mensaje Cargado"})
#         else:
#             return render (request, "AppMensajeria/crearMensaje.html", {"mensaje" : "ERROR: No cargado"})
#     else:
#         formulario=Message()
#         return render(request, "AppMensajeria/crearMensaje.html", {"formulario": formulario})