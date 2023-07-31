from django.urls import path
from . import views

urlpatterns = [
    path("", views.Target_Schools.as_view()),
    path("<int:pk>", views.Target_SchoolDetail.as_view()),
]
