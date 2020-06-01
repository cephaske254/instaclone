from .models import Profile, User
from django import forms


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =['user']

class UpdateDetailsForm(forms.ModelForm):
    class Meta:
        model = User
        exclude=[]
