from django.urls import path
from .views import Followings, FollowingDetail, FollowingToggle

urlpatterns = [
    path("", Followings.as_view()),
    path("<int:pk>", FollowingDetail.as_view()),
    path("<int:pk>/tracks/<int:track_pk>", FollowingToggle.as_view()),
]
