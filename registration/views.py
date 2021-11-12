from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator



# Create your views here.

class RegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class LoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('homepage')

class LogoutView(LogoutView):
    redirect_field_name = 'homepage'
    next_page = None
    template_name = "index.html"