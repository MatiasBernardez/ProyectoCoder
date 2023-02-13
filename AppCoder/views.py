from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso


# Create your views here.
def inicio(request):
    return HttpResponse("Vista inicio")

def cursos(request):
    return HttpResponse("Vista cursos")

def profesores(request):
    return HttpResponse("Vista profesores")

def entregables(request):
    return HttpResponse("Vista entregables")

def estudiantes(request):
    return HttpResponse("Vista estudiantes")