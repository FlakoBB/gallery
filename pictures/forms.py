from django import forms
from .models import Picture

class PictureRegistrationForm(forms.ModelForm):
  class Meta:
    model = Picture
    fields = ['image', 'title', 'description', 'album']
