from django.urls import path
from .views import QuestionListAPIView, QuestionDetailAPIView

from django.urls import path
from .views import (
    QuestionListAPIView,
    QuestionDetailAPIView,
    QuestionCreateAPIView,
    QuestionUpdateAPIView,
    QuestionDeleteAPIView,
)

urlpatterns = [
    path("", QuestionListAPIView.as_view()),
    path("<int:external_id>/", QuestionDetailAPIView.as_view()),

    # 🔐 Admin işlemleri
    path("create/", QuestionCreateAPIView.as_view()),
    path("<int:external_id>/update/", QuestionUpdateAPIView.as_view()),
    path("<int:external_id>/delete/", QuestionDeleteAPIView.as_view()),
]

