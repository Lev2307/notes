from django.urls import path

from .views import (
    CreateNoteView,
    ReadNotesView,
    UpdateNoteView,
    DeleteNoteView
)

urlpatterns = [
    path('read/', ReadNotesView.as_view(), name='read_notes'),
    path('create/', CreateNoteView.as_view(), name='create_note'),
    path('read/delete_note/<int:pk>/', DeleteNoteView.as_view(), name='delete_note'),
    path('read/edit_note/<int:pk>/', UpdateNoteView.as_view(), name='edit_note'),
]