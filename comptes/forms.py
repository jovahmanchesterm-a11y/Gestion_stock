from django import forms
from django.contrib.auth.models import User
from .models import image

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password','image']

class imageForm(forms.ModelForm):
    class Meta:
        model = image
        fields = ['photo']


