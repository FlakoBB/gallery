from django.urls import path
from . import views

urlpatterns = [
  path('registrar-imagen/', views.picture_registration_view, name='picture_registration'),
  path('crear-album/', views.create_album, name='create_album'),
  path('albumes/', views.show_albums, name='albums'),
  path('albumes/<str:album_name>', views.show_album_pictures, name='album_pictures')
]
