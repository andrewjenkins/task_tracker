from django import forms
from django.contrib.auth.models import User

MIN_USERNAME_LENGTH = 3
MAX_USERNAME_LENGTH = 30
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 256

class RegisterForm(forms.Form):
    username = forms.CharField(min_length=MIN_USERNAME_LENGTH, max_length=MAX_USERNAME_LENGTH)
    password = forms.CharField(min_length=MIN_PASSWORD_LENGTH, max_length=MAX_PASSWORD_LENGTH)
    email = forms.EmailField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists.')
        return email
