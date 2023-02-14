from django import forms


#Especificar los campos

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    comision = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    asignatura = forms.CharField(max_length=30)