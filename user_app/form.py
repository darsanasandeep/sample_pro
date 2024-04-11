from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Register, UploadImage


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['first_name', 'last_name', 'age', 'email']


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']


class UserImageForm(forms.ModelForm):

    class Meta:
        models = UploadImage
        fields = ['caption','image']