from django.db import models

# Create your models here.
class Integrante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    mail= models.EmailField()
    area_investigacion=models.TextField()
    ingreso=models.DateTimeField(null=True)
    avatar=models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f' {self.id}-{self.nombre}-{self.apellido}'
    
class Publicacion(models.Model):
    titulo= models.CharField(max_length=250)
    autores=models.CharField(max_length=100)
    revista=models.CharField(max_length=30)
    volumen=models.IntegerField()
    anio=models.IntegerField()
    def __str__(self):
        return f' {self.id}-{self.titulo}-{self.autores}-{self.revista}-{self.volumen}-{self.anio}'
   
    
class Colaborador(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    mail=models.EmailField()
    universidad=models.CharField(max_length=30)
    def __str__(self):
        return f' {self.id}-{self.nombre}-{self.apellido}.{self.universidad}'
    
    