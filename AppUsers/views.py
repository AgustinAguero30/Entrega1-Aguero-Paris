from django.shortcuts import render
from AppTienda.models import *
from AppTienda.forms import *
from django.contrib.auth.decorators import login_required
from AppUsers.forms import *
from AppTienda.views import obtenerAvatar
#Users CRUD
#Read
def leerUsuarios(request):
    usuarios=User.objects.all()
    for usuario in usuarios:
        lista= Avatar.objects.filter(user=usuario)
        if len(lista)!=0:
            usuario.avatar=lista[0].imagen.url
        else:
            usuario.avatar= "/media/avatares/NoAvatar.png"
    return render(request, "AppUsers/leerUsuarios.html", {"usuarios":usuarios})
#Update
@login_required
def editarUsuario(request, id):
    usuario=User.objects.get(id=id)
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            usuario.username=informacion["username"]
            usuario.last_name=informacion["last_name"]
            usuario.first_name=informacion["first_name"]
            usuario.email=informacion["email"]                
            usuario.save()
            usuarios=User.objects.all()
            return render (request, "AppUsers/leerUsuarios.html", {"usuarios":usuarios})
    else:
        form=UserEditForm(initial={"username":usuario.username, "apellido":usuario.last_name, "nombre":usuario.first_name, "email":usuario.email})
        return render(request, "AppUsers/editarUsuario.html", {"formulario":form, "usuario":usuario})
#Delete
@login_required
def eliminarUsuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    #Despues de eliminar, volvemos a guardar todos los objetos restantes para mostrarlos
    usuarios=User.objects.all()
    return render(request,"AppUsers/leerUsuarios.html", {"usuarios":usuarios})#Mostrar