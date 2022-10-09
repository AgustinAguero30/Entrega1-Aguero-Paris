
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    last_name = forms.CharField(label="Ingrese Apellido")
    first_name = forms.CharField(label="Ingrese Nombre")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name','first_name']
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    
    last_name = forms.CharField(label="Modificar Apellido")
    first_name = forms.CharField(label="Modificar Nombre")
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2','last_name','first_name']
        help_texts={k:"" for k in fields}