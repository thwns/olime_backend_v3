from django.urls import path
from .views import Workbooks, WorkbookDetail

urlpatterns = [
    path("", Workbooks.as_view()),
    path("<int:pk>", WorkbookDetail.as_view()),
]
