from django.urls import path
from .views import NoteListCreate, NoteDetail

urlpatterns = [
    path('', NoteListCreate.as_view(), name='notes-list'),
    path('<int:pk>/', NoteDetail.as_view(), name='notes-detail'),
]
