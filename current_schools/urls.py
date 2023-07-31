from django.urls import path
from . import views

urlpatterns = [
    path("", views.Current_Schools.as_view()),
    path("<int:pk>", views.Current_SchoolDetail.as_view()),
]
