from django import forms

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
    imagen= forms.ImageField(label="Imagen")    

class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")    

