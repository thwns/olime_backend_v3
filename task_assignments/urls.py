from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskAssignmentViewSet

router = DefaultRouter()
router.register(r'task_assignments', TaskAssignmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
