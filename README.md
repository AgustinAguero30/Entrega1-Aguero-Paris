# Entrega1-Aguero-Paris
---------------------------------Requerimientos de Sistema para ejecutar Proyecto Tienda-----------------------------------------------

- Visual Studio Code
- Python
- Django
- DB Browser SqLite
- Navegador Web

---------------------------------Instalacion de Proyecto Tienda en Visual Studio Code desde un github---------------------------------

1. Desde la terminal de VSC tipeamos "git clone" y la direccion del git del Proyecto Tienda
2. Nos ubicamos en el Proyecto Tienda donde se encuentra el manage.py 
3. Correr el servidor con "python manage.py runserver"
4. Ya esta listo para su visualizacion en la IP Local

---------------------------------Funcionalidades de nuestra APP------------------------------------------------------------------------
 
Mostrar en un Inicio las distintas templates las cuales permite: 
Generar carga de articulos en nuestra base de datos.
Busqueda de articulos cargados mediante un identificador.

Descripcion de views.py dentro de AppTienda

- Incluye las definiciones de mostrar los templates correspondiente renderizados cuando son llamados mediante urls

Ejemplo:

def clientes(request):
    return render(request,"AppTienda/clientes.html")


- Incluye ademas las definiciones las cuales reciben mediante POST una informacion cargada en un formulario para posteriormente ser guardadas en la base de datos.

Ejemplo:

def clientes(request):
    if request.method == "POST": #Confirma si recibe la informacion por POST, valida el formulario, limpia informacion y guarda en variable
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

- Incluye las definiciones de buscar en nuestra base de datos informacion que el usuario proporciona mediante un formulario de consulta.

Ejemplo:

def buscarCliente(request):
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        clientes=Cliente.objects.filter(apellido=apellido) #Traer de la base todos los clientes que tengan este apellido
        
        return render(request, "AppTienda/resultadosBusquedaClientes.html", {"clientes":clientes}) #Envia informacion encontrada a template para poder trabajar en como se mostrara los datos
    else:
        return render(request, "AppTienda/busquedaClientes.html", {"mensaje":"Ingrese nuevamente apellido"}) # Si no encuentra, envia nuevamente a la pagina de busqueda y envia mensaje para su reingreso de informacion


Descripcion de models.py dentro de AppTienda

- Aqui generamos los esqueletos de las tablas que se guardaran en nuestra base de datos.

Ejemplo:

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.IntegerField()
    mail=models.EmailField()

    def __str__(self):
        return self.nombre + " " + self.apellido   # Como se nombra si es llamado

Descripcion de forms.py dentro de AppTienda

- Aqui generamos las vistas de como se mostraran los campos de nuestros formularios en las templates

class ClientesForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    telefono=forms.IntegerField()
    mail=forms.EmailField()

Descripcion de urls.py dentro de AppTienda

- Aqui generamos los path y a que definicion llamaria mediante nuestro Proyecto desde la web.

Ejemplo:

"http://127.0.0.1:8000/AppTienda/clientes/ (Mediante esta url, llama a la def clientes donde esta codificada la funcion "Cargar cliente"

    path('', inicio, name="inicio"),
    path('clientes/', clientes, name="clientes"),
    path('zapatillas/', zapatillas, name="zapatillas"),
    path('remeras/', remeras, name="remeras"),
    path('pantalones/', pantalones, name="pantalones"),




-------------------------------- Descripcion de la web ----------------------------------------

Desde "http://127.0.0.1:8000/AppTienda/" (Inicio)

Funcionalidad de Botonera: Tienda / Inicio / Clientes / Zapatillas / Remeras / Pantalones / Busqueda de Articulos (Clientes Zapatillas Remeras Pantalones)

Tienda: Redirige a Inicio
Inicio: Redirige a Inicio

--------

Clientes: Muestra formulario de carga de clientes
Zapatillas: Muestra formulario de carga de zapatillas
Remeras: Muestra formulario de carga de remeras
Pantalones: Muestra formulario de carga de pantalones

--------

Busqueda de Articulos (Menu desplegable)

Clientes: Muestra formulario de busqueda de clientes por apellido. (Lista con Apellido, Nombre, Telefono)
Zapatillas: Muestra formulario de busqueda de zapatillas por marca. (Lista con Modelo, Marca, Talle, Precio)
Remeras: Muestra formulario de busqueda de remeras por marca. (Lista con Modelo, Marca, Talle, Precio) **Talle 1: S, Talle 2: M, Talle 3: L, Talle 4: XL, Talle 5: XXL
Pantalones: Muestra formulario de busqueda de pantalones por marca. (Lista con Modelo, Marca, Talle, Precio)

-----------------------------------------Autores------------------------------------------------
Agustin Aguero 
Agustin Paris

