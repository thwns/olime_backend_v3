from django.urls import path
from . import views

urlpatterns = [
    path("", views.Contents.as_view()),
    path("<int:pk>", views.ContentDetail.as_view()),
    path("books/", views.Books.as_view()),
    path("books/<int:pk>", views.BookDetail.as_view()),
    path("lectures/", views.Lectures.as_view()),
    path("lectures/<int:pk>", views.LectureDetail.as_view()),
]
