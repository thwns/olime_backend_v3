from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskDayViewSet

router = DefaultRouter()
router.register(r'task_day', TaskDayViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
