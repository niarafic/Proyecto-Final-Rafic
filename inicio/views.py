from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    template=loader.get_template('inicio.html')
    template_renderizado=template.render({})
    return HttpResponse(template_renderizado)
