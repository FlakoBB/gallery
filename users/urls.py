from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
  path('acceder/', views.login_view, name='login'),
  path('salir/', views.logout_view, name='logout'),
  path('inicio/', TemplateView.as_view(template_name='users/mypictures.html'), name='home')
]
