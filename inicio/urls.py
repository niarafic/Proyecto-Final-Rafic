from django.urls import path
from inicio.views import inicio, integrantes, crear_integrantes
urlpatterns = [
    path('', inicio, name='inicio'), 
    path('integrantes/', integrantes, name='integrantes'), 
    path('integrantes/crear', crear_integrantes, name='crear_integrantes'),
    
]
