from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Workbook_EvaluationViewSet

router = DefaultRouter()
router.register(r'workbook_evaluation', Workbook_EvaluationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]