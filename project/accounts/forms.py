from django import forms
from . import models 
from django.contrib.auth.models import User


class User_Form(forms.ModelForm):
    class Meta:
        forms = User
        fields = ['username', 'firs_name', 'last_name', 'email']

class Profile_Form(forms.ModelForm):
    class Meta:
        forms = User
        fields = ['image', 'country', 'address']