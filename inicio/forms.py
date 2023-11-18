from django import forms
class BaseIntegrante(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    mail=forms.CharField(max_length=30)
    area_investigacion=forms.CharField(max_length=250)
    ingreso=forms.DateTimeField()
    
    

# Formulario para crear un integrante
class CrearIntegrante(BaseIntegrante):
    ...
    
class ActualizarIntegrante(BaseIntegrante):
    avatar=forms.ImageField(required=False)
   
   
# Formulario para crear una publicación   
class CrearPublicacion(forms.Form):
    titulo= forms.CharField(max_length=250)
    autores=forms.CharField(max_length=100)
    revista=forms.CharField(max_length=30)
    volumen=forms.IntegerField()
    anio=forms.IntegerField()
    
#Formulario para la búsqueda de una publicación
class BusquedaPublicacionFormulario(forms.Form):
    titulo=forms.CharField(max_length=250, required=False)


# Formulario para crear un colaborador  
class CrearColaborador(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    mail=forms.EmailField()
    universidad=forms.CharField(max_length=30)
    