from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


#Especificar los campos

class CursoFormulario(LoginRequiredMixin, forms.Form):
    curso = forms.CharField()
    comision = forms.IntegerField()

class ProfesorFormulario(LoginRequiredMixin, forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    asignatura = forms.CharField(max_length=30)

class EstudianteFormulario(LoginRequiredMixin, forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class EntregablesFormulario(LoginRequiredMixin, forms.Form):
    nombre = forms.CharField(max_length=30)
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()



class UserRegisterForm(LoginRequiredMixin, UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}