from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth.views import LoginView


# Create your views here.

class RegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('homepage')

class LoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('homepage')