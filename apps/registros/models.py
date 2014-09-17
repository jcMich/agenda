from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Grupos(models.Model):
    user = models.ForeignKey(User)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)

    def __str__(self):
        return self.nombre

class Registros(models.Model):
    def url(self,filename):
        ruta = "static/MultimediaData/Registros/%s/%s"%(str(self.id),filename)
        return ruta
    user = models.ForeignKey(User)
    grupo = models.ForeignKey(Grupos,default=1)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100,null=True,blank=True)
    imagen = models.ImageField(upload_to=url,null=True,blank=True)
    telefono = models.CharField(max_length=50)
    nota = models.TextField(max_length=500,null=True,blank=True)


    def __str__(self):
        return "%s %s"%(self.nombre,self.apellidos)