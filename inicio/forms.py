from django import forms

class CrearIntegrante(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    mail=forms.CharField(max_length=30)
    area_investigacion=forms.CharField(max_length=250)
    
    