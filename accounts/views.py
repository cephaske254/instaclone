from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django_registration.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.http.response import HttpResponseRedirect
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request,'django_registration/registration_form.html', {'form':form})