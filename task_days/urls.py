from django.urls import path
from .views import Task_Days, Task_DayDetail

urlpatterns = [
    path("", Task_Days.as_view()),
    path("<int:pk>", Task_DayDetail.as_view()),
]
