from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskEvaluationViewSet

router = DefaultRouter()
router.register(r'task_evaluation', TaskEvaluationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
