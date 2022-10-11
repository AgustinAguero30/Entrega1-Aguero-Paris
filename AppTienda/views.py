from datetime import datetime
from django.shortcuts import render
from AppTienda.models import *
from AppTienda.forms import *
from django.contrib.auth.decorators import login_required



# Create your views here.

#####-----------Llamo al render y le pego los HTML-----------####
@login_required
def inicio(request):
    return render(request,"AppTienda/inicio.html", {"avatar":obtenerAvatar(request)})

def zapatillas(request):
    return render(request,"AppTienda/zapatillas.html",{"avatar":obtenerAvatar(request)})

#####----------- Crear formularios para guardar en la base de datos -----------####

def zapatillas(request):
    if request.method == "POST":
#Ya que los articulos tienen informacion similar, los juntamos en un solo formulario.         
        form=ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            informacion= form.cleaned_data
            modelo=informacion["modelo"]
            marca=informacion["marca"]
            talle=informacion["talle"]
            precio=informacion["precio"]
            imagen=informacion["imagen"]
            date=datetime.now().date() 
            zapatilla=Zapatilla(modelo=modelo, marca=marca,talle=talle,precio=precio,imagen=imagen,date=date,user= request.user)           
            zapatilla.save()
            zapatillas=Zapatilla.objects.all()
            return render (request, "AppTienda/leerZapatillas.html", {"zapatillas":zapatillas, "mensaje" : "Zapatilla Cargada"})
        else:
            return render (request, "AppTienda/inicio.html", {"mensaje" : "ERROR: No cargada"})
    else:
        formulario=ArticuloForm()
        return render(request, "AppTienda/zapatillas.html", {"formulario": formulario})


def busquedaZapatillas(request):
    return render(request,"AppTienda/busquedaZapatillas.html",{"avatar":obtenerAvatar(request)})


def buscarZapatilla(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        zapatillas=Zapatilla.objects.filter(marca=marca)
        
        return render(request, "AppTienda/resultadosBusquedaZapatillas.html", {"zapatillas":zapatillas})
    else:
        return render(request, "AppTienda/busquedaZapatillas.html", {"mensaje":"Ingrese nuevamente marca"})

#Zapatillas CRUD
#Read
def leerZapatillas(request):
    zapatillas=Zapatilla.objects.all()
    return render(request, "AppTienda/leerZapatillas.html", {"zapatillas":zapatillas})

#Update
@login_required
def editarZapatilla(request, id):
    zapatilla=Zapatilla.objects.get(id=id)
    if request.method=="POST":
        form=ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            informacion= form.cleaned_data
            zapatilla.modelo=informacion["modelo"]
            zapatilla.marca=informacion["marca"]
            zapatilla.talle=informacion["talle"]
            zapatilla.precio=informacion["precio"]
            zapatilla.imagen=informacion["imagen"]
            date=datetime.now().date()        
            zapatilla.save()
            zapatillas=Zapatilla.objects.all()     
            return render (request, "AppTienda/leerZapatillas.html", {"zapatillas":zapatillas})
    else:
        form=ArticuloForm(initial={"modelo":zapatilla.modelo, "marca":zapatilla.marca, "talle":zapatilla.talle, "precio":zapatilla.precio, 'imagen':zapatilla.imagen})
        return render(request, "AppTienda/editarZapatilla.html", {"formulario":form, "zapatilla":zapatilla})
#Delete
@login_required
def eliminarZapatilla(request, id):
    zapatilla = Zapatilla.objects.get(id=id)
    zapatilla.delete()
    #Despues de eliminar, volvemos a guardar todos los objetos restantes para mostrarlos
    zapatillas=Zapatilla.objects.all()
    return render(request,"AppTienda/leerZapatillas.html", {"zapatillas":zapatillas})#Mostrar

def infoZapatilla(request, id):
    zapatilla=Zapatilla.objects.get(id=id)
    return render(request, "AppTienda/infoZapatilla.html", {"zapatilla":zapatilla})
#---------------------------------------------------------------------------------------------------#

#CRUD Avatar
@login_required
def agregarAvatar(request):
    if request.method=='POST':
        formulario = AvatarForm(request.POST, request.FILES)
        print(formulario)
        if formulario.is_valid():
            avatarViejo = Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo[0].delete()
            avatar = Avatar(user = request.user, imagen= formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request,"AppTienda/inicio.html", {'mensaje':"Avatar Agregado", "usuario":request.user, 'imagen': avatar.imagen.url})
        else:
            return render(request,"AppTienda/agregarAvatar.html", {"formulario":formulario, 'mensaje': "invalido"})

    else:
        formulario=AvatarForm()
        return render(request,"AppTienda/agregarAvatar.html", {"formulario":formulario, "usuario":request.user})

def obtenerAvatar(request):
    lista= Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar= "/media/avatares/NoAvatar.png"
    return avatar  