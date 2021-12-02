from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, Http404
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from django.views.generic import (
                                  CreateView,
                                  ListView,
                                  UpdateView,
                                  DeleteView,
                                    )
from .models import (
                     Note,
                     Collection,
                        )

from .forms import (
                    CreateCollectionModelForm,
                    CreateNoteModelForm,
                        )
import math



# Create your views here.

class HomePageView(View):
    template_name = 'index.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user = request.user
        return render(request, 'index.html', {'profile': user})


class CreateNoteView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = CreateNoteModelForm
    template_name = 'notes/create_note.html'
    success_url = reverse_lazy('read_notes')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class UpdateNoteView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = CreateNoteModelForm
    template_name = 'notes/edit_note.html'
    success_url = reverse_lazy('read_notes')

class DeleteNoteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/delete_note.html'
    success_url = reverse_lazy('read_notes')
    context_object_name = 'notes'

class ReadNotesView(LoginRequiredMixin, ListView):
    template_name = 'notes/read_notes.html'
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        notes = Note.objects.filter(user = request.user)
        collections = Collection.objects.filter(user=request.user)
        page = int(request.GET.get('page', 1))
        start_index = (page * self.paginate_by) - self.paginate_by
        end_index = page * self.paginate_by
        pages_count = math.ceil(len(notes) / self.paginate_by)

        if page > 0:
            if page > pages_count:
                return redirect(f'/notes/read/?page={pages_count}')
            elif page < 1:
                return redirect('/notes/read/?page=1')
        else:
            return render(request, 'notes/read_notes.html')

        return render(request, 'notes/read_notes.html', {'notes_list': notes[start_index:end_index],
                                                         'collections': collections,
                                                         'current_page': page,
                                                         'next': page + 1,
                                                         'prev': page - 1,
                                                         'pages_count': pages_count,
                                                         'pages_count_list': range(1, pages_count+1)})

def create_collection(request):
    form = CreateCollectionModelForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            collection = form.save(commit=False)
            collection.user = request.user
            collection.save()
            return HttpResponse(collection.name)
        else:
            return render(request, "notes/collection_create_form.html", context={
                "form": form
            })

    return render(request, 'notes/read_notes.html', {
                                                    'form': form,
    })

def create_collection_form(request):
    form = CreateCollectionModelForm()
    context = {
        "form": form
    }
    return render(request, "notes/collection_create_form.html", context)

