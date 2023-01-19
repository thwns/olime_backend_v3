from django.urls import path
from . import views

urlpatterns = [
    path("", views.Followlists.as_view()),
    path("<int:pk>", views.FollowlistDetail.as_view()),
]
