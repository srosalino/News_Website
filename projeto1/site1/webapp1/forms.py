from django import forms

from django.contrib.auth.forms import UserCreationForm


class FormUser1(UserCreationForm):
    username = forms.CharField(label='Indique o seu nome de utilizador', min_length=5, max_length=50)
    email = forms.EmailField(label='Indique o seu email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Introduza a sua password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a sua password', widget=forms.PasswordInput)


class FormUserLogin(UserCreationForm):
    username = forms.CharField(label='Indique o seu nome de utilizador', min_length=5, max_length=50)
    password1 = forms.CharField(label='Introduza a sua password', widget=forms.PasswordInput)
