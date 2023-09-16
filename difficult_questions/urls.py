from django.urls import path
from .views import Difficult_QuestionsView, Difficult_QuestionDetailView

urlpatterns = [
    path("", Difficult_QuestionsView.as_view()),
    path("<int:pk>/", Difficult_QuestionDetailView.as_view()),
]
