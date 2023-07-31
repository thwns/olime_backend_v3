from django.urls import path
from . import views

urlpatterns = [
    path("", views.Early_Decisions.as_view()),
    path("<int:pk>", views.Early_DecisionDetail.as_view()),
]
