from django.urls import path
from Congresos.views import ListadoCongresos, CrearCongreso, ActualizarCongreso, EliminarCongreso, DetalleCongreso 

urlpatterns=[
    path('congresos/', ListadoCongresos.as_view() ,name='congresos'),
    path('congresos/crear/', CrearCongreso.as_view(), name='crear_congreso'),
    path('congresos/<int:pk>/', DetalleCongreso.as_view(), name='detalle_congreso'),
    path('congresos/<int:pk>/actualizar/', ActualizarCongreso.as_view(), name='actualizar_congreso'),
    path('congresos/<int:pk>/eliminar', EliminarCongreso.as_view(), name='eliminar_congreso')
]
