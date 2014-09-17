from django.db import models
from django.contrib.auth.models import User

#perfil de usuario
class userProfile(models.Model):
    def url(self, filename):
        ruta = 'static/MultimediaData/Usuarios/%s/%s'%(self.user.username,filename)
        return ruta
    user = models.OneToOneField(User)
    photo = models.ImageField(upload_to=url,null=True,blank=True)

    def __str__(self):
        return self.user.username
