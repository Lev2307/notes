from django.urls import path

from .views import (
    CreateNoteView,
    ReadNotesView,
    UpdateNoteView,
    DeleteNoteView,
    CreateCollection,
)

urlpatterns = [
    path('read/', ReadNotesView.as_view(), name='read_notes'),
    path('create/', CreateNoteView.as_view(), name='create_note'),
    path('delete/<int:pk>/', DeleteNoteView.as_view(), name='delete_note'),
    path('edit/<int:pk>/', UpdateNoteView.as_view(), name='edit_note'),
    path('collections/create/', CreateCollection.as_view(), name='create_collection')
]