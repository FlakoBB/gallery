from django.urls import path
from . import views

urlpatterns = [
  path('registrar-imagen/', views.picture_registration_view, name='picture_registration'),
]
