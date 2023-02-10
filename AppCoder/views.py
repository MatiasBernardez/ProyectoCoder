from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso


# Create your views here.
def curso(self):
    curso = Curso(nombre="Desarrollo Web", comision=19881)
    curso.save()
    documentoDeTexto = f"--> Curso: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(documentoDeTexto)