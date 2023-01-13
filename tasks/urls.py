from django.urls import path
from . import views

urlpatterns = [
    path("", views.see_all_tasks),
    path("<int:task_id>", views.see_one_task),
]
