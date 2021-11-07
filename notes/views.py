from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
from registration.views import LoginView
from registration.forms import RegisterForm
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

class HomePageView(View):
    template_name = 'index.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user = request.user
        return render(request, 'index.html', {'profile': user})