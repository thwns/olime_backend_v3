from django.urls import path
from . import views

urlpatterns = [
    path("", views.Regular_Decisions.as_view()),
    path("<int:pk>", views.Regular_DecisionDetail.as_view()),
]
