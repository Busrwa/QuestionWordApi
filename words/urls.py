from django.urls import path
from .views import (
    WordListView,
    WordCreateView,
    WordDetailView,
    WordUpdateView,
    WordDeleteView,
)

urlpatterns = [
    path('words/', WordListView.as_view(), name='word-list'),
    path('words/add/', WordCreateView.as_view(), name='word-add'),
    path('words/<int:pk>/', WordDetailView.as_view(), name='word-detail'),
    path('words/<int:pk>/update/', WordUpdateView.as_view(), name='word-update'),
    path('words/<int:pk>/delete/', WordDeleteView.as_view(), name='word-delete'),
]
