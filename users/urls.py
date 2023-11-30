from django.urls import path
from . import views
from pictures.views import show_all_pictures

urlpatterns = [
  path('acceder/', views.login_view, name='login'),
  path('salir/', views.logout_view, name='logout'),
  path('', show_all_pictures, name='home'),
  path('registrar/', views.register_view, name='register'),
]
