from django import forms

class FormularioContacto(forms.Form):

    nombre=forms.CharField(label='Nombre', required=True, max_length=100)
    email=forms.EmailField(label='Email', required=True, max_length=100)
    contenido=forms.CharField(label='Contenido', required=False, max_length=1000, widget=forms.Textarea)
    