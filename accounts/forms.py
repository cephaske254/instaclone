from .models import Profile, User
from django import forms


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =['user']

class UpdateDetailsForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    
