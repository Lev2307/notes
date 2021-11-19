
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView

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

class CreateNoteView(CreateView):
    template_name = 'notes/create.html'
    success_url = '/notes/read/'

    def get(self, request, *args, **kwargs):
        form = CreateNoteModelForm(request.POST or None)
        return render(request, 'notes/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateNoteModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return render(request, 'notes/create.html', {"form": form,
                                                         'obj': obj})

class ReadNotesView(ListView):
    template_name = 'notes/read.html'

    def get(self, request, *args, **kwargs):
        qs = Note.objects.all()
        page = int(request.GET.get('page', 1))
        paginate_by = 6
        start_index = (page * paginate_by) - paginate_by
        end_index = page * paginate_by
        pages_count = math.ceil(len(qs) / paginate_by)
        
        if page > pages_count:
            return redirect(f'/notes/read/?page={pages_count}')
        elif page < 1:
            return redirect('/notes/read/?page=1')

        return render(request, 'notes/read.html', {'data_list': qs[start_index:end_index],
                                                   'next': page + 1,
                                                   'prev': page - 1,
                                                   'pages_count': pages_count,
                                                   'pages_count_list': range(1, pages_count+1)})

    