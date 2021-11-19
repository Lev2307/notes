from django.urls import path

from .views import (
    CreateNoteView,
    ReadNotesView,
)

urlpatterns = [
    path('read/', ReadNotesView.as_view(), name='read_notes'),
    path('create/', CreateNoteView.as_view(), name='create_note'),

]