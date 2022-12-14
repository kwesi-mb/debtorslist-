from django.forms import ModelForm 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email']

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    occupation = forms.CharField(max_length = 100)
    residential_address = forms.CharField(max_length=100)
    gender = forms.CheckboxInput()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'gender', 'occupation', 'residential_address', 'email', 'password1', 'password2')