from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, ModelForm

from main_app.models import *


class RegisterForm(UserCreationForm):
    username = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2"]
        widgets = {
            "first_name": TextInput(attrs={"placeholder": "Imię"}),
            "last_name": TextInput(attrs={"placeholder": "Nazwisko"}),
            "username": TextInput(attrs={"placeholder": "Email"}),
            "password1": TextInput(attrs={"placeholder": "Hasło"}),
            "password2": TextInput(attrs={"placeholder": "Powtórz hasło"})
        }


class LoginForm(forms.Form):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput(attrs={"placeholder": "Hasło"}))
