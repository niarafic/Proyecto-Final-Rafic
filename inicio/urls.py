from django.urls import path
from inicio.views import inicio, integrantes, crear_integrantes, publicaciones, crear_publicaciones, colaboradores, crear_colaboradores, eliminar_integrantes, actualizar_integrantes, detalle_integrantes
urlpatterns = [
    path('', inicio, name='inicio'), 
    path('integrantes/', integrantes, name='integrantes'), 
    path('integrantes/crear', crear_integrantes, name='crear_integrantes'),
    path('integrantes/<int:integrante_id>/eliminar', eliminar_integrantes, name='eliminar_integrantes'),
    path('integrantes/<int:integrante_id>/actualizar', actualizar_integrantes, name='actualizar_integrantes'),
    path('integrantes/<int:integrante_id>/', detalle_integrantes, name='detalle_integrantes'),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('publicaciones/crear', crear_publicaciones, name='crear_publicaciones'),
    path('colaboradores/', colaboradores, name='colaboradores'),
    path('colaboradores/crear', crear_colaboradores, name='crear_colaboradores'),
    
]
