from django.shortcuts import render
from AppTienda.models import *
from django.http import HttpResponse
from AppTienda.forms import *
# Create your views here.

#####-----------Llamo al render y le pego los HTML-----------####

def inicio(request):
    return render(request,"AppTienda/inicio.html")

def clientes(request):
    return render(request,"AppTienda/clientes.html")

def zapatillas(request):
    return render(request,"AppTienda/zapatillas.html")

def remeras(request):
    return render(request,"AppTienda/remeras.html")

def pantalones(request):
    return render(request,"AppTienda/pantalones.html")

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
            return render (request, "AppTienda/inicio.html")

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
            return render (request, "AppTienda/inicio.html")
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
            return render (request, "AppTienda/inicio.html")
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
            return render (request, "AppTienda/inicio.html")
    else:
        formulario=ArticuloForm()
        return render(request, "AppTienda/pantalones.html", {"formulario": formulario})


def busquedaClientes(request):
    return render(request,"AppTienda/busquedaClientes.html")


def buscar(request):
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        clientes=Cliente.objects.filter(apellido=apellido) #Traer de la base todos los clientes que tengan este apellido
        
        return render(request, "AppCoder/resultadosBusquedaClientes.html", {"clientes":clientes})
    else:
        return render(request, "AppCoder/busquedaClientes.html", {"mensaje":"Ingrese nuevamente apellido"})

