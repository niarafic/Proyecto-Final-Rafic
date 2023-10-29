from django.db import models

# Create your models here.
class Integrante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    mail= models.CharField(max_length=30)
    area_investigacion=models.TextField()
    def __str__(self):
        return f' {self.id}-{self.nombre}-{self.apellido}'
    
    