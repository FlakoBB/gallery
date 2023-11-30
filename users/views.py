from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout

def login_view(request):
  if request.user.is_authenticated:
    # ToDo: handle when the user is authenticated already
    pass

  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)
        return redirect('home')

  else:
    form = AuthenticationForm()

  return render(request, 'users/login.html', {'form': form})

def logout_view(request):
  logout(request)
  return redirect('login')

def register_view(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)

    if form.is_valid():
      form.save()
      return redirect('home')

  else:
    form = UserRegistrationForm()

  return render(request, 'users/register.html', {'form': form})
