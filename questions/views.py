from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .models import Question
from .serializers import QuestionSerializer
from .pagination import QuestionPagination


# 🔓 Herkes erişebilir — kategoriye göre liste
class QuestionListAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]
    pagination_class = QuestionPagination

    def get_queryset(self):
        queryset = Question.objects.all()

        category = self.request.query_params.get("category")
        if category:
            queryset = queryset.filter(category__iexact=category)

        return queryset


# 🔓 Herkes erişebilir — id'ye göre tek soru
class QuestionDetailAPIView(generics.RetrieveAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]
    lookup_field = "external_id"
    queryset = Question.objects.all()


# 🔐 SADECE ADMIN — soru ekleme
class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


# 🔐 SADECE ADMIN — soru güncelleme
class QuestionUpdateAPIView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = "external_id"


# 🔐 SADECE ADMIN — soru silme
class QuestionDeleteAPIView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = "external_id"
