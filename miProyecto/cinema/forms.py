from django import forms

class Registro_usuario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()

class BusquedaPeliculaForm(forms.Form):
    movie = forms.CharField(max_length=100, label='Buscar película')

