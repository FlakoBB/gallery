from django.shortcuts import render, redirect
from .forms import PictureRegistrationForm

def picture_registration_view(request):
  if request.method == 'POST':
    form = PictureRegistrationForm(request.POST, request.FILES)

    if form.is_valid():
      form.save()
      return redirect('home')

  else:
    form = PictureRegistrationForm()

  return render(request, 'pictures/picture_registration.html', {'form': form})
