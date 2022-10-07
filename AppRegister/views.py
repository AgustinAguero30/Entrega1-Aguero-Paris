from django.shortcuts import render
from AppRegister.models import *
from django.http import HttpResponse
from AppRegister.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

#Register

def register(request):
    if request.method=="POST":
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            form.save()
            return render(request, "AppTienda/inicio.html", {"mensaje": f"usuario {username}"} ) 
        else:
            return render(request, "AppRegister/register.html" , { 'formulario':form, "mensaje":"incorrecto" })
    else:
        form=UserRegisterForm()
        return render(request, "AppRegister/register.html" , { 'formulario':form })       


@login_required
def editarPerfil(request):

    #Instancia del login
    usuario = request.user

    #Si es metodo POST hago lo mismo que el agregar

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data

            #Datos que se modifican
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "AppTienda/inicio.html",{"mensaje": "Se ha modificado la contraseña correctamente"}) #Vuelvo al inicio o a donde se desee
        else:
            return render(request, "AppRegister/editarPerfil.html",{"formulario":miFormulario, "usuario":usuario, "mensajes": "Formulario invalido, vuelva a ingresar"} )
#En el caso que no sea POST
    else:
        #Creo el formulario de los datos que voy a modificar
        miFormulario=UserEditForm(instance=usuario)

    #Voy al html que me permite editar
        return render(request, "AppRegister/editarPerfil.html", {"formulario":miFormulario, "usuario":usuario})
