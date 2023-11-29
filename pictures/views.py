from django.shortcuts import render, redirect, get_object_or_404
from .forms import PictureRegistrationForm
from .models import Picture, Album

def picture_registration_view(request):
  if request.method == 'POST':
    form = PictureRegistrationForm(request.POST, request.FILES)

    if form.is_valid():
      form.save()
      return redirect('home')

  else:
    form = PictureRegistrationForm()

  return render(request, 'pictures/picture_registration.html', {'form': form})

def show_all_pictures(request):
  pictures = Picture.objects.all()
  return render(request, 'users/mypictures.html', {'pictures': pictures})

def show_albums(request):
  albums = Album.objects.all()
  albums_with_last_picture = []

  for album in albums:
    last_picture = Picture.objects.filter(album=album).last()
    albums_with_last_picture.append({'album': album, 'last_picture':last_picture})
  return render(request, 'pictures/albums.html', {'albums': albums_with_last_picture})

def show_album_pictures(request, album_name):
  album = get_object_or_404(Album, name=album_name)
  album_pictures = Picture.objects.filter(album=album)

  return render(request, 'pictures/album_pictures.html', {'album': album, 'pictures': album_pictures})
