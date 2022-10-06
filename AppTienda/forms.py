from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Como se visualizan los campos de nuestros formularios en las templates.

class ClientesForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    telefono=forms.IntegerField()
    mail=forms.EmailField()

class ArticuloForm(forms.Form):
    modelo=forms.CharField(max_length=50)
    marca=forms.CharField(max_length=50)
    talle=forms.IntegerField()
    precio=forms.IntegerField()

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts={k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")

