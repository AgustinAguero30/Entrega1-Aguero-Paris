from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserEditForm(UserCreationForm):
    
    username = forms.CharField()
    last_name = forms.CharField()
    first_name = forms.CharField()
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name','username']
        help_texts={k:"" for k in fields}