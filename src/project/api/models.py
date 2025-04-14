from django.db import models

# Create your models here.

class Tarea(models.Model):
    titulo = models.CharField(max_length= 50)
    descripcion = models.TextField(blank= True)
    hecha = models.BooleanField(default= False)

    def __str__(self):
        return self.titulo