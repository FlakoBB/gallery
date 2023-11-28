from django.db import models
import os

class Album(models.Model):
  name = models.CharField(max_length=150, default='Nameless Album', help_text='Nombre del album')
  description = models.CharField(max_length=300, help_text='Descripcion del album', blank=True, null=True)
  is_public = models.BooleanField(default=True)

  def __str__(self):
    return self.name

class Picture(models.Model):
  image = models.ImageField(upload_to='images/')
  title = models.CharField(max_length=150, default='Nameless Picture', help_text='Titulo de la imagen')
  description = models.CharField(max_length=300, help_text='descripcion de la imagen', blank=True, null=True)
  album = models.ForeignKey(Album, help_text='A que album pertenece', blank=True, null=True, on_delete=models.SET_NULL)

  def delete(self, using=False, keep_parents=False):
    if self.image:
      if os.path.isfile(self.image.path):
        os.remove(self.image.path)

    super().delete(using=using, keep_parents=keep_parents)

  def __str__(self):
    return self.title
