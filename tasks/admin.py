from django.contrib import admin
from .models import Task


@admin.action(description="Set all learning_time to zero")
def reset_learning_time(model_admin, request, tasks):
    for task in tasks.all():
        task.learning_time = 0
        task.save()


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    actions = (reset_learning_time,)

    list_display = (
        "name",
        "ranges",
        "rating",
        "learning_time",
        "track",
    )
    search_fields = (
        "name",
        "rating",
        "owner__",
    )

    # ^ : startswith
    # = : exact
