from django.shortcuts import render, redirect, get_object_or_404
from .forms import PictureRegistrationForm, AlbumRegistrationForm
from .models import Picture, Album
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

@login_required(login_url=reverse_lazy('login'))
def picture_registration_view(request):
  if request.method == 'POST':
    form = PictureRegistrationForm(request.POST, request.FILES)

    if form.is_valid():
      form.save()
      return redirect('home')

  else:
    form = PictureRegistrationForm()

  return render(request, 'pictures/picture_registration.html', {'form': form})

@login_required(login_url=reverse_lazy('login'))
def show_all_pictures(request):
  pictures = Picture.objects.all()
  return render(request, 'users/mypictures.html', {'pictures': pictures})

@login_required(login_url=reverse_lazy('login'))
def create_album(request):
  if request.method == 'POST':
    form = AlbumRegistrationForm(request.POST)

    if form.is_valid:
      form.save()
      return redirect('albums')

  else:
    form = AlbumRegistrationForm()

  return render(request, 'pictures/create_album.html', {'form': form})

@login_required(login_url=reverse_lazy('login'))
def show_albums(request):
  albums = Album.objects.all()
  albums_with_last_picture = []

  for album in albums:
    last_picture = Picture.objects.filter(album=album).last()
    albums_with_last_picture.append({'album': album, 'last_picture':last_picture})
  return render(request, 'pictures/albums.html', {'albums': albums_with_last_picture})

@login_required(login_url=reverse_lazy('login'))
def show_album_pictures(request, album_name):
  album = get_object_or_404(Album, name=album_name)
  album_pictures = Picture.objects.filter(album=album)

  return render(request, 'pictures/album_pictures.html', {'album': album, 'pictures': album_pictures})
