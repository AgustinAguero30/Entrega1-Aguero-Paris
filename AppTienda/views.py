from django.shortcuts import render
from AppTienda.models import *
from AppTienda.forms import *
from django.contrib.auth.decorators import login_required



# Create your views here.

#####-----------Llamo al render y le pego los HTML-----------####
@login_required
def inicio(request):
    return render(request,"AppTienda/inicio.html", {"avatar":obtenerAvatar(request)})

def clientes(request):
    return render(request,"AppTienda/clientes.html",{"avatar":obtenerAvatar(request)})

def zapatillas(request):
    return render(request,"AppTienda/zapatillas.html",{"avatar":obtenerAvatar(request)})

def remeras(request):
    return render(request,"AppTienda/remeras.html",{"avatar":obtenerAvatar(request)})

def pantalones(request):
    return render(request,"AppTienda/pantalones.html",{"avatar":obtenerAvatar(request)})

#####----------- Crear formularios para guardar en la base de datos -----------####

def clientes(request):
    if request.method == "POST":
        form=ClientesForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            telefono=informacion["telefono"]
            mail=informacion["mail"]
#Guardamos la informacion obtenida en una variable         
            cliente=Cliente(nombre=nombre, apellido=apellido,telefono=telefono,mail=mail)
#Guardamos en la base de datos con save y devolvemos a la pagina inicio cuando todo este correctamente cargado.            
            cliente.save()
            return render (request, "AppTienda/inicio.html", {"mensaje" : "Cliente Cargado"})

#Si no se cargo correctamente, vuelve a mostrar el formulario a cargar vacio 
    else:
        formulario=ClientesForm()
        return render(request, "AppTienda/clientes.html", {"formulario": formulario})

def zapatillas(request):
    if request.method == "POST":
#Ya que los articulos tienen informacion similar, los juntamos en un solo formulario.         
        form=ArticuloForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            modelo=informacion["modelo"]
            marca=informacion["marca"]
            talle=informacion["talle"]
            precio=informacion["precio"]      
            zapatilla=Zapatilla(modelo=modelo, marca=marca,talle=talle,precio=precio)           
            zapatilla.save()
            return render (request, "AppTienda/inicio.html", {"mensaje" : "Zapatilla Cargada"})
    else:
        formulario=ArticuloForm()
        return render(request, "AppTienda/zapatillas.html", {"formulario": formulario})

def remeras(request):
    if request.method == "POST":     
        form=ArticuloForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            modelo=informacion["modelo"]
            marca=informacion["marca"]
            talle=informacion["talle"]
            precio=informacion["precio"]      
            remera=Remera(modelo=modelo, marca=marca,talle=talle,precio=precio)           
            remera.save()
            return render (request, "AppTienda/inicio.html", {"mensaje" : "Remera Cargada"})
    else:
        formulario=ArticuloForm()
        return render(request, "AppTienda/remeras.html", {"formulario": formulario})   

def pantalones(request):
    if request.method == "POST":        
        form=ArticuloForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            modelo=informacion["modelo"]
            marca=informacion["marca"]
            talle=informacion["talle"]
            precio=informacion["precio"]      
            pantalon=Pantalon(modelo=modelo, marca=marca,talle=talle,precio=precio)           
            pantalon.save()
            return render (request, "AppTienda/inicio.html", {"mensaje" : "Pantalon Cargado"})
    else:
        formulario=ArticuloForm()
        return render(request, "AppTienda/pantalones.html", {"formulario": formulario})


def busquedaClientes(request):
    return render(request,"AppTienda/busquedaClientes.html",{"avatar":obtenerAvatar(request)})

def busquedaZapatillas(request):
    return render(request,"AppTienda/busquedaZapatillas.html",{"avatar":obtenerAvatar(request)})

def busquedaRemeras(request):
    return render(request,"AppTienda/busquedaRemeras.html",{"avatar":obtenerAvatar(request)})

def busquedaPantalones(request):
    return render(request,"AppTienda/busquedaPantalones.html",{"avatar":obtenerAvatar(request)})


def buscarCliente(request):
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        clientes=Cliente.objects.filter(apellido=apellido) #Traer de la base todos los clientes que tengan este apellido
        
        return render(request, "AppTienda/resultadosBusquedaClientes.html", {"clientes":clientes})
    else:
        return render(request, "AppTienda/busquedaClientes.html", {"mensaje":"Ingrese nuevamente apellido"})

def buscarZapatilla(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        zapatillas=Zapatilla.objects.filter(marca=marca)
        
        return render(request, "AppTienda/resultadosBusquedaZapatillas.html", {"zapatillas":zapatillas})
    else:
        return render(request, "AppTienda/busquedaZapatillas.html", {"mensaje":"Ingrese nuevamente marca"})

def buscarRemera(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        remeras=Remera.objects.filter(marca=marca)
        
        return render(request, "AppTienda/resultadosBusquedaRemeras.html", {"remeras":remeras})
    else:
        return render(request, "AppTienda/busquedaRemeras.html", {"mensaje":"Ingrese nuevamente marca"})

def buscarPantalon(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        pantalones=Pantalon.objects.filter(marca=marca)
        
        return render(request, "AppTienda/resultadosBusquedaPantalones.html", {"pantalones":pantalones})
    else:
        return render(request, "AppTienda/busquedaPantalones.html", {"mensaje":"Ingrese nuevamente marca"})

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
        form=ArticuloForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            zapatilla.modelo=informacion["modelo"]
            zapatilla.marca=informacion["marca"]
            zapatilla.talle=informacion["talle"]
            zapatilla.precio=informacion["precio"]                
            zapatilla.save()
            zapatillas=Zapatilla.objects.all()
            return render (request, "AppTienda/leerZapatillas.html", {"zapatillas":zapatillas})
    else:
        form=ArticuloForm(initial={"modelo":zapatilla.modelo, "marca":zapatilla.marca, "talle":zapatilla.talle, "precio":zapatilla.precio})
        return render(request, "AppTienda/editarZapatilla.html", {"formulario":form, "zapatilla":zapatilla})
#Delete
@login_required
def eliminarZapatilla(request, id):
    zapatilla = Zapatilla.objects.get(id=id)
    zapatilla.delete()
    #Despues de eliminar, volvemos a guardar todos los objetos restantes para mostrarlos
    zapatillas=Zapatilla.objects.all()
    return render(request,"AppTienda/leerZapatillas.html", {"zapatillas":zapatillas})#Mostrar

#---------------------------------------------------------------------------------------------------#

#CRUD Avatar
@login_required
def agregarAvatar(request):
    if request.method=='POST':
        formulario = AvatarForm(request.POST, request.FILES)
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
        avatar= ""
    return avatar  