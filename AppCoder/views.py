from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor, Estudiante, Entregable
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregablesFormulario
from django.views.generic import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
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
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], asignatura=informacion['asignatura'])
            profesor.save()
            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario = ProfesorFormulario()

    return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})


def estudiantes(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            estudiante.save()
            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario = EstudianteFormulario()

    return render(request, "AppCoder/estudiantes.html", {"miFormulario":miFormulario})


def entregables(request):
    if request.method == 'POST':
        miFormulario = EntregablesFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            entregable = Entregable(nombre=informacion['nombre'], fechaDeEntrega=informacion['fechaDeEntrega'], entregado=informacion['entregado'])
            entregable.save()
            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario = EntregablesFormulario()

    return render(request, "AppCoder/entregables.html", {"miFormulario":miFormulario})




def busquedaComision(request):

    return render(request, "AppCoder/busquedaComision.html")


def buscarComision(request):

    if request.GET["comision"]:

        #respuesta = f"Estoy buscando la comision nro: {request.GET['comision']}"
        comision = request.GET["comision"]
        cursos = Curso.objects.filter(comision__icontains=comision)

        return render(request, "AppCoder/inicio.html", {"cursos":cursos, "comision":comision})

    else:

        respuesta = "No enviaste datos"


    #return HttpResponse(respuesta)
    return render(request, "AppCoder/inicio.html", {"respuesta":respuesta})


def leerProfesores(request):

    profesores = Profesor.objects.all()

    contexto = {"profesores":profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)


def eliminarProfesor(request, profesor_nombre):

    profesor = Profesor.objects.get(nombre = profesor_nombre)
    profesor.delete()

    profesores = Profesor.objects.all()

    contexto = {"profesores":profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)


def editarProfesor(request, profesor_nombre):

    profesor = Profesor.objects.get(nombre = profesor_nombre)

    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.asignatura = informacion['asignatura']

            profesor.save()

            return render(request, "AppCoder/inicio.html")

    else:
        miFormulario = ProfesorFormulario(initial = {'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'asignatura':profesor.asignatura})

    return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})



class CursoList(ListView):
    model = Curso
    template_name = "AppCoder/cursos_list.html"

class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'comision']

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'comision']

class CursoDelete(DeleteView):
    model = Curso
    success_url = "/AppCoder/Curso/list"



def login_request(request):


    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)


        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)


            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bievenido {usuario}"} )
            else:

                return render(request, "AppCoder/inicio.html", {"mensaje":"Error, datos incorrectos"} )

        else:

                return render(request, "AppCoder/inicio.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {'form':form})


def register(request):

    if request.method == 'POST':

        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":"Usuario Creado :)"})

    else:
        #form = UserCreationForm()
        form = UserRegisterForm()

    return render(request, "AppCoder/registro.html", {"form":form})