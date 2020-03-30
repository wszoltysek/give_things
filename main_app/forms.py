from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, ModelForm

from main_app.models import *


class RegisterForm(UserCreationForm):
    username = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Imię'}),
            'last_name': TextInput(attrs={'placeholder': 'Nazwisko'}),
            'username': TextInput(attrs={'placeholder': 'Email'}),
            'password1': TextInput(attrs={'placeholder': 'Hasło'}),
            'password2': TextInput(attrs={'placeholder': 'Powtórz hasło'})
        }


class LoginForm(forms.Form):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = [
            'quantity', 'address', 'city', 'zip_code', 'phone_number',
            'pick_up_date', 'pick_up_time', 'pick_up_comment'
        ]
