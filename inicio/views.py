from django.shortcuts import render, redirect
from inicio.models import Integrante
from inicio.forms import CrearIntegrante

# Create your views here.
def inicio(request):
    return render(request, 'inicio/inicio.html')

def integrantes(request):

    return render(request, 'inicio/integrantes.html')

def crear_integrantes(request):
    """ if request.method=='POST':
        nombre=request.POST.get('Nombre')
        apellido=request.POST.get('Apellido')
        mail=request.POST.get('Mail')
        area_investigacion=request.POST.get('Área de Investigación')   
        integrante= Integrante(nombre=nombre, apellido=apellido, mail=mail, area_investigacion=area_investigacion)
        integrante.save() """
    if request.method=='POST':
        formulario=CrearIntegrante(request.POST)
        if formulario.is_valid():
            info_limpia=formulario.cleaned_data
            nombre=info_limpia.get('nombre')
            apellido=info_limpia.get('apellido')
            mail=info_limpia.get('mail')
            area_investigacion=info_limpia.get('area_investigacion')
            integrante= Integrante(nombre=nombre, apellido=apellido, mail=mail, area_investigacion=area_investigacion)
            integrante.save()
            
            return redirect('integrantes')
        else:
            return render(request,'inicio/crear_integrantes.html',{'formulario':formulario})
            
     
        
    formulario=CrearIntegrante()
    return render(request,'inicio/crear_integrantes.html',{'formulario':formulario})
    
