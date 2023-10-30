from django.shortcuts import render, redirect
from inicio.models import Integrante, Colaborador, Publicacion
from inicio.forms import CrearIntegrante, CrearPublicacion, CrearColaborador

# Vista de inicio
def inicio(request):
    return render(request, 'inicio/inicio.html')


# Vista de integrantes del laboratorio
def integrantes(request):
    
    #buscar_apellido=request.GET.get('apellido')
    
    # if buscar_apellido:
    #     listado_integrantes=Integrante.objects.filter(apellido__icontains=buscar_apellido)
        
    # else:
    
    #     listado_integrantes=Integrante.objects.all()

    listado_integrantes=Integrante.objects.all()
    return render(request, 'inicio/integrantes.html', {'listado_integrantes': listado_integrantes})

# Vista para la creación de integrantes
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


# Vista para publicaciones
    
def publicaciones(request):
    
    buscar_titulo=request.GET.get('titulo')
    
    if buscar_titulo:
        listado_publicaciones=Publicacion.objects.filter(titulo__icontains=buscar_titulo)
        
    else:
    
        listado_publicaciones=Publicacion.objects.all()

    return render(request, 'inicio/publicaciones.html', {'listado_publicaciones': listado_publicaciones})

#vista de crear publicaciones

def crear_publicaciones(request):
    if request.method=='POST':
        formulario=CrearPublicacion(request.POST)
        if formulario.is_valid():
            info_limpia=formulario.cleaned_data
            titulo=info_limpia.get('titulo')
            autores=info_limpia.get('autores')
            volumen=info_limpia.get('volumen')
            anio=info_limpia.get('anio')
            publicacion= Publicacion(titulo=titulo, autores=autores, volumen=volumen, anio=anio)
            publicacion.save()
                     
            return redirect('publicaciones')
        else:
            return render(request,'inicio/crear_publicaciones.html',{'formulario':formulario})
            
     
        
    formulario=CrearPublicacion()
    return render(request,'inicio/crear_publicaciones.html',{'formulario':formulario})


#Vista de Colaboradores


def colaboradores(request):
    buscar_apellido=request.GET.get('apellido')
    
    if buscar_apellido:
        listado_colaboradores=Colaborador.objects.filter(apellido__icontains=buscar_apellido)
        
    else:
    
        listado_colaboradores=Colaborador.objects.all()

    return render(request, 'inicio/colaboradores.html', {'listado_colaboradores':listado_colaboradores})

#vista para la creación de colaboradores





def crear_colaboradores(request):
    if request.method=='POST':
        formulario=CrearColaborador(request.POST)
        if formulario.is_valid():
            info_limpia=formulario.cleaned_data
            nombre=info_limpia.get('nombre')
            apellido=info_limpia.get('apellido')
            mail=info_limpia.get('mail')
            universidad=info_limpia.get('universidad')
            colaborador= Colaborador(nombre=nombre, apellido=apellido, mail=mail, universidad=universidad)
            colaborador.save()
                     
            return redirect('colaboradores')
        else:
            return render(request,'inicio/crear_colaboradores.html',{'formulario':formulario})
            
     
        
    formulario=CrearColaborador()
    return render(request,'inicio/crear_colaboradores.html',{'formulario':formulario})

