from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    telefono=models.IntegerField()
    mail=models.EmailField()

    def __str__(self):
        return self.nombre + " " + self.apellido   

class Zapatilla(models.Model):
    modelo=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    talle=models.IntegerField()
    precio=models.IntegerField()

    def __str__(self):
        return self.modelo + " " + self.marca

class Remera(models.Model):
    modelo=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    talle=models.IntegerField()
    precio=models.IntegerField()

    def __str__(self):
        return self.modelo + " " + self.marca

class Pantalon(models.Model):
    modelo=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    talle=models.IntegerField()
    precio=models.IntegerField()

    def __str__(self):
        return self.modelo + " " + self.marca