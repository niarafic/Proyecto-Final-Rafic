from django.urls import path
from inicio.views import inicio, integrantes, crear_integrantes, publicaciones, crear_publicaciones, colaboradores, crear_colaboradores
urlpatterns = [
    path('', inicio, name='inicio'), 
    path('integrantes/', integrantes, name='integrantes'), 
    path('integrantes/crear', crear_integrantes, name='crear_integrantes'),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('publicaciones/crear', crear_publicaciones, name='crear_publicaciones'),
    path('colaboradores/', colaboradores, name='colaboradores'),
    path('colaboradores/crear', crear_colaboradores, name='crear_colaboradores'),
    
]
