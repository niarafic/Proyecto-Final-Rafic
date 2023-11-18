from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from Congresos.models import Congreso
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class ListadoCongresos(ListView):
    model = Congreso
    context_object_name='listado_congresos'
    template_name='congresos/congresos.html'
    
    
class CrearCongreso(LoginRequiredMixin, CreateView):
    model= Congreso
    template_name='congresos/crear_congreso.html'
    fields=[ 'nombre_congreso', 'lugar', 'pais', 'anio',    'rol']
    success_url= reverse_lazy('congresos')
    
  
class ActualizarCongreso(LoginRequiredMixin, UpdateView):
    model= Congreso
    template_name='congresos/actualizar_congreso.html'
    fields=[ 'nombre_congreso', 'lugar', 'pais', 'anio',    'rol']
    success_url= reverse_lazy('congresos')
    
   
class DetalleCongreso(DetailView):
    model=Congreso
    template_name="congresos/detalle_congreso.html"
    
class EliminarCongreso(LoginRequiredMixin, DeleteView):
    model=Congreso
    template_name="congresos/eliminar_congreso.html"
    success_url= reverse_lazy('congresos')