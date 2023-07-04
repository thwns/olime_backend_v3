from django.urls import path
from . import views

urlpatterns = [
    path("", views.Workbook_Evaluations.as_view()),
    path("<int:pk>", views.Workbook_EvaluationDetail.as_view()),
]
