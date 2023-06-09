from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()

class Estudiante(models.Model): 
    nombre=models.CharField(max_length=40)  
    apellido=models.CharField(max_length=40)  
    email=models.EmailField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)  
    apellido=models.CharField(max_length=40)  
    email=models.EmailField()
    materia=models.CharField(max_length=40) 

class Actividades(models.Model):
    nombre=models.CharField(max_length=40)  
    FechaDeEntrega=models.DateField()
    entregado=models.BooleanField()
    
