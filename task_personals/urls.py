from django.urls import path
from .views import Task_PersonalView, Task_PersonalDetailView

urlpatterns = [
    path("", Task_PersonalView.as_view()),
    path("<int:pk>/", Task_PersonalDetailView.as_view()),
]
