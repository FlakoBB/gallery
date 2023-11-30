from django import forms
from .models import Picture, Album

class PictureRegistrationForm(forms.ModelForm):
  class Meta:
    model = Picture
    fields = ['image', 'title', 'description', 'album']

class AlbumRegistrationForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = ['name', 'description']
