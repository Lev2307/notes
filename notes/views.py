from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'index.html')