from django.urls import path
from .views import Lovings, LovingDetail, LovingToggle

urlpatterns = [
    path("", Lovings.as_view()),
    path("<int:pk>", LovingDetail.as_view()),
    path("<int:pk>/tracks/<int:track_pk>", LovingToggle.as_view()),
]
