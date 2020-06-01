from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login,logout, authenticate
from django_registration.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, decorators
from django.http.response import HttpResponseRedirect
from .forms import UpdateProfileForm, UpdateDetailsForm
from .models import Profile
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

@decorators.login_required
def update_profile(request):
    profile_form = UpdateProfileForm()
    details_form = UpdateDetailsForm()
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES)
        details_form = UpdateDetailsForm(request.POST)

        if profile_form.is_valid():
            Profile.save_profile(request.user,profile_form.cleaned_data.get('bio'),request.FILES['profile_image'])

        return redirect('profile',username=request.user.username)
    return render(request, 'update_profile.html',{
        'title': f'Update Profile | @{request.user}',
        'profile_form':profile_form,
        'details_form':details_form,
    })