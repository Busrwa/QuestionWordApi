from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied

from .models import Word
from .serializers import WordSerializer
from .filters import WordFilter


# Pagination
class WordPagination(PageNumberPagination):
    page_size = 10

from rest_framework.permissions import AllowAny


# Listeleme
class WordListView(generics.ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [AllowAny]  # 🔓 Şifresiz erişim
    filter_backends = [DjangoFilterBackend]
    filterset_class = WordFilter
    pagination_class = WordPagination


# Kelime Ekleme (SADECE ADMIN)
class WordCreateView(generics.CreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


# Detay Görüntüleme (ADMIN + VIEWER)
class WordDetailView(generics.RetrieveAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticated]


# Güncelleme (SADECE ADMIN)
class WordUpdateView(generics.UpdateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


# Silme (SADECE ADMIN)
class WordDeleteView(generics.DestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
