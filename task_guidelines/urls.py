from django.urls import path
from .views import TaskGuidelineListCreateView, TaskGuidelineDetailView

urlpatterns = [
    path('', TaskGuidelineListCreateView.as_view(),
         name='task-guideline-list-create'),
    path('<int:pk>/', TaskGuidelineDetailView.as_view(),
         name='task-guideline-detail'),
]
