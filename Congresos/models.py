from django.db import models


class Congreso(models.Model):
    nombre_congreso=models.CharField(max_length=50)
    lugar=models.CharField(max_length=50)
    pais=models.CharField(max_length=50)
    anio=models.IntegerField()
    rol=models.CharField(max_length=20)
    logo=models.ImageField(upload_to='logos', null=True, blank=True)
    def __str__(self):
        return f'{self.nombre_congreso}-{self.lugar}'   
