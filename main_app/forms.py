from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, forms, TextInput


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Imię'}),
            'last_name': TextInput(attrs={'placeholder': 'Nazwisko'}),
            'email': TextInput(attrs={'placeholder': 'Email'}),
            'password1': TextInput(attrs={'placeholder': 'Hasło'}),
            'password2': TextInput(attrs={'placeholder': 'Powtórz hasło'}),
        }
