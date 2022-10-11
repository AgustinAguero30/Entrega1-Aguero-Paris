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

 Tienda en la cual se pueden registar Usuarios, agregar un avatar personalizado, editar informacion de usuario, editar Avatar.
 Agregar Zapatilla, Buscar Zapatilla, Editar Zapatilla, Leer Mas.
 
Botones:
 
Boton: Tienda | Usuario:Deslogueado	Redirigir a Login	Redirige a Login
Boton: Tienda | Usuario:Logueado	Redirigir a Inicio	Redirige a Inicio

Boton: Comunidad | Usuario:Deslogueado	Redirigir a Listado de Usuarios	Redirige a Listado de Usuario
Boton: Comunidad | Usuario:Logueado	Redirigir a Listado de Usuarios	Redirige a Listado de Usuario

Boton: Zapatilla | Usuario:Deslogueado	Redirigir a Zapatillas	Redirige a Zapatillas
Boton: Zapatilla  | Usuario:Logueado	Redirigir a Zapatillas	Redirige a Zapatillas

Boton: Iniciar Sesion | Usuario: Deslogueado	Tiene que aparecer y redirigir a Login	Aparece y Redirige a Login
Boton: Iniciar Sesion | Usuario: Logueado	No tiene que aparecer	No Aparece

Boton: Registrarse | Usuario: Deslogueado 	Tiene que aparecer y redirige a Register	Aparece y Redirige a Register
Boton: Registrarse | Usuario: Logueado	No tiene que aparecer	No Aparece

Boton: Desloguearse | Usuario: Deslogueado	No tiene que aparecer	No Aparece
Boton: Desloguearse | Usuario: Logueado	Tiene que aparecer,  tiene que desloguear y avisar por pantalla	Aparece, desloguea y avisa por pantalla

Boton: About Us | Usuario: Deslogueado	Tiene que aparecer y redirigir a aboutUs	Aparece y redirge a aboutUs
Boton: About Us | Usuario: Logueado	Tiene que aparecer y redirigir a aboutUs	Aparece y redirge a aboutUs

Boton: Agregar Articulo | Usuario: Deslogueado	No tiene que aparecer	No Aparece
Boton: Agregar Articulo | Usuario: Logueado	Despliega Submenu y muestra opcion: Zapatilla	Despliega Submenu y muetra boton Zapatilla

Boton:  Zapatillas (Desplegado de Agregar Articulo) | Usuario: Logueado	Redirigir a Cargar nueva Zapatilla	Redirige a Cargar nueva Zapatilla

Boton: Perfil | Usuario: Deslogueado	No tiene que aparecer	No Aparece
Boton: Perfil | Usuario: Logueado	Despliega Submenu y muestra opcion: Editar Perfil / Cambiar Avatar	Despliega Submenu y muetra Editar Perfil / Cambiar Avatar

Boton:  Zapatillas (Desplegado de Editar Perfil) | Usuario: Logueado	Redirigir a Editar Perfil	Redirige a Editar Perfil
Boton:  Zapatillas (Desplegado de Cambiar Avatar) | Usuario: Logueado	Redirigir a Cambiar Avatar	Redirige a Cambiar Avatar

Boton: Buscar en leerZapatillas | Usuario: Deslogueado	Redirigir a listado filtrado por marca o Solicitar nuevo ingreso si es incorrecto	Redirige en caso de ser correcto y avisa por caso contrario
Boton: Buscar en leerZapatillas | Usuario: Logueado	Redirigir a listado filtrado por marca o Solicitar nuevo ingreso si es incorrecto	Redirige en caso de ser correcto y avisa por caso contrario

Boton: LeerMas en leerZapatillas	Redirigir a InfoZapatilla	Redige a Info Zapatilla

En About Us, Boton Tienda	Redirigir a Tienda	Redirige a Tienda
En About Us, Boton Inicio	Redirigir a Tienda	Redirige a Tienda
En About Us, Agustin Aguero	Situa en informacion de Agustin Aguero	Situa correctamente a Agustin Aguero
En About Us, Agustin Paris	Situa en informacion de Agustin Paris	Situa correctamente a Agustin Paris
En About Us, Boton: Git	Redirige a perfil correspondiente del boton	Redirige correctamente dependiendo la persona
En About Us, Agustin Paris Boton: Linkedin	Redirige a perfil correspondiente del boton	Redirige correctamente dependiendo la persona

En Login, Iniciar Sesion	Redirigir a Pantalla de Bievenida	Redirige a pantalla de Bienvendida

En infoZapatilla siendo Admin Boton: Editar, Eliminar	Solamente a admin mostrar. Eliminar: Borra zapatilla y redirige a leerZapatilla, Editar: Redirige a Editar zapatilla	Muestra solamente a Admin, redirige correctamente y elimina objeto con el boton eliminar

--------------------------------------- Forma de Trabajo en equipo ---------------------------------

Nos coordinamos para realizar reuniones en la cual se avanzaba a la par, se pensaron las funcionalidades en conjunto. Lo comun era que uno del equipo comparta pantalla y se distribuyeran las tareas. Luego de comprobar la funcionalidad, se juntaba el codigo y se limpiaba el mismo.

Tuvimos la oportunidad de poder avanzar siempre en sincronia, por lo que nos sirvio para asentar el conocimiento y despejando las dudas que surgian.

-----------------------------------------Autores------------------------------------------------


Agustin Aguero / 
Agustin Paris
