from django.db import models
from django.utils import  timezone


#definimos el modelo Post
#models.Model significa que el Post es un modelo Django, así que Django sabe que debe ser guardado en la base de datos.
class Post(models.Model):

    autor=models.ForeignKey('auth.User')
    titulo=models.CharField(max_length=300)
    text0=models.TextField()

    fecha_creacion=models.DateField(default=timezone.now())#por defecto va a estar puesto la fecha actual del ordenador

    fecha_publicacion=models.DateField(blank=True,null=True)#la fecha de creacion es opcional (blank=True,null=True)


    #el siguiente metodo publica el post
    def publicar(self):
        self.fecha_publicacion=timezone.now()#le damos un valor a la fecha de publicacion
        self.save()

    #como se visualizara  nuestro post en el Administrador de Django
    def __str__(self):
        return self.titulo


