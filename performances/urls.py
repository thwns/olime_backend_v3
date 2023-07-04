from django.urls import path
from . import views

urlpatterns = [
    path("", views.Performances.as_view()),
    path("<int:pk>", views.PerformanceDetail.as_view()),
]
