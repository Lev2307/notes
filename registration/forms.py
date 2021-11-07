from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UsernameField

class RegisterForm(UserCreationForm):
    username = UsernameField(
        label='',
    )
    email = forms.EmailField(label='',)
    password1 = forms.CharField(label='', 
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='', 
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }