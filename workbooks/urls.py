from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkbookViewSet

router = DefaultRouter()
router.register(r'workbook', WorkbookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]