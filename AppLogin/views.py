from django.shortcuts import render
from AppLogin.models import *
from AppLogin.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

# Create your views here.

#Login
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST['username']
            clave=request.POST['password']

            usuario= authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppTienda/inicio.html")
            else:
                return render(request, "AppLogin/login.html", {"formulario":form, "mensaje":"incorrecto"})
        else:
            return render(request, "AppLogin/login.html", {"formulario":form, "mensaje":"incorrecto"})

    else:
        form = AuthenticationForm()
        return render(request, "AppLogin/login.html", {"formulario":form})

