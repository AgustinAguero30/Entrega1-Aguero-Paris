from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Zapatilla(models.Model):
    modelo=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    talle=models.IntegerField()
    precio=models.IntegerField()
    #Subcarpeta zapatillas de media
    imagen= models.ImageField(upload_to='productos', null=True)
    date= models.DateField(null=True)
    user = models.ForeignKey(User, null=True, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.modelo + " " + self.marca

class Avatar(models.Model):
    #Vinculo con el usuario
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    #Subcarpeta avatares de media
    imagen= models.ImageField(upload_to='avatares')