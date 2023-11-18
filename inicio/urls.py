from django.urls import path
from inicio.views import inicio, integrantes, crear_integrantes, publicaciones, crear_publicaciones, colaboradores, crear_colaboradores, EliminarIntegrante, ActualizarIntegrante, detalle_integrantes, about
urlpatterns = [
    path('', inicio, name='inicio'), 
    path('about/', about, name='about'), 
    path('integrantes/', integrantes, name='integrantes'), 
    path('integrantes/crear', crear_integrantes, name='crear_integrantes'),
    path('integrantes/<int:pk>/actualizar', ActualizarIntegrante.as_view(), name='actualizar_integrantes'),
    path('integrantes/<int:pk>/eliminar', EliminarIntegrante.as_view(), name='eliminar_integrantes'),
    path('integrantes/<int:integrante_id>/', detalle_integrantes, name='detalle_integrantes'),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('publicaciones/crear', crear_publicaciones, name='crear_publicaciones'),
    path('colaboradores/', colaboradores, name='colaboradores'),
    path('colaboradores/crear', crear_colaboradores, name='crear_colaboradores'),
    
]




#path('integrantes/<int:integrante_id>/actualizar', , name='actualizar_integrantes'),
#path('integrantes/<int:integrante_id>/eliminar', eliminar_integrantes, name='eliminar_integrantes'),
