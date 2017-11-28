from django import forms
 
class PostForm(forms.Form):
    numero_doc = forms.CharField(max_length=50)
    nombres = forms.CharField(max_length=150)
    apellidos = forms.CharField(max_length=150)
    genero = forms.CharField(max_length=150)
    edad = forms.CharField(max_length=150)

class EgresadoForm(forms.Form):
    numero_doc = forms.CharField(max_length=50)
    nombre = forms.CharField(max_length=150)
    apellido = forms.CharField(max_length=150)
    genero = forms.CharField(max_length=150)
    edad = forms.CharField(max_length=150)