from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')
    #return HttpResponse("vista inicio")

def cursos(request):
    return render(request, 'AppCoder/cursos.html')
    #return HttpResponse("vista cursos")

def profesores(request):
    return render(request, 'AppCoder/profesores.html')
    #return HttpResponse("vista profesores")

def entregables(request):
    return render(request, 'AppCoder/entregables.html')
    #return HttpResponse("vista entregables")

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')
    #return HttpResponse("vista estudiantes")


def cursoFormulario(request):
    return render(request, 'AppCoder/cursoFormulario.html')
    #return HttpResponse("vista estudiantes")

"""
Esto solo fue una prueba, ya no es necesario par ael proyecto

def curso(self):
    curso = Curso(nombre="Desarrollo web", comision=19881)
    curso.save()
    documentoDeTexto = f'--> Curso:{curso.nombre} comision:{curso.comision}'
    return HttpResponse(documentoDeTexto)

"""
