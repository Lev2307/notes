from django.http import request
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .forms import CreateNoteModelForm
import math

# Create your views here.

class HomePageView(View):
    template_name = 'index.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user = request.user
        return render(request, 'index.html', {'profile': user})


class CreateNoteView(LoginRequiredMixin, CreateView):
    template_name = 'notes/create.html'

    def get(self, request, *args, **kwargs):
        form = CreateNoteModelForm(request.POST or None)
        user = request.user
        return render(request, 'notes/create.html', {'form': form, 'profile': user})

    def post(self, request, *args, **kwargs):
        form = CreateNoteModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return render(request, 'notes/create.html', {"form": form,'obj': obj})

class ReadNotesView(LoginRequiredMixin, ListView):
    template_name = 'notes/read.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        qs = Note.objects.all()
        page = int(request.GET.get('page', 1))
        start_index = (page * self.paginate_by) - self.paginate_by
        end_index = page * self.paginate_by
        pages_count = math.ceil(len(qs) / self.paginate_by)

        if page > pages_count:
            return redirect(f'/notes/read/?page={pages_count}')
        elif page < 1:
            return redirect('/notes/read/?page=1')

        return render(request, 'notes/read.html', { 'notes_list': qs[start_index:end_index],
                                                    'current_page': page,
                                                    'next': page + 1,
                                                    'prev': page - 1,
                                                    'pages_count': pages_count,
                                                    'pages_count_list': range(1, pages_count+1)})
    