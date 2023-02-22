from django.db import models

# Create your models here, estas son las tablas que voy a tener en la bd y lo de adentro es los campos que se van a tener.

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    

"""
Esto es para cargar a la bd, todo esto lo puedo hacer en el shell
from AppCoder.models import Curso
curso = Curso(nombre="Phyton", comision=23800)
curso.save()


"""