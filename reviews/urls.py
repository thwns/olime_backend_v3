from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/replys", views.ReviewReplys.as_view()),
    path("<int:pk>", views.ReviewDetail.as_view()),
]
