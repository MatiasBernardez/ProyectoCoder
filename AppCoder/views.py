from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario


# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/inicio.html')
    #return HttpResponse("Vista inicio")

def cursos(request):
    return render(request, 'AppCoder/cursos.html')
    #return HttpResponse("Vista cursos")

def profesores(request):
    return render(request, 'AppCoder/profesores.html')
    #return HttpResponse("Vista profesores")

def entregables(request):
    return render(request, 'AppCoder/entregables.html')
    #return HttpResponse("Vista entregables")

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')
    #return HttpResponse("Vista estudiantes")



def cursos(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], comision=informacion['comision'])
            curso.save()
            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursos.html", {"miFormulario":miFormulario})


def profesores(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion["email"], asignatura=informacion["asignatura"])
            profesor.save()
            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario = ProfesorFormulario()

    return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})


def busquedaComision(request):

    return render(request, "AppCoder/busquedaComision.html")


def buscar(request):

    if request.GET["comision"]:

        #respuesta = f"Estoy buscando la comision nro: {request.GET['comision']}"
        comision = request.GET["comision"]
        cursos = Curso.objects.filter(comision__icontains=comision)

        return render(request, "AppCoder/inicio.html", {"cursos":cursos, "comision":comision})

    else:

        respuesta = "No enviaste datos"


    #return HttpResponse(respuesta)
    return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})