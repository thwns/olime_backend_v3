from django.contrib import admin
from .models import Task_Personal


@admin.register(Task_Personal)
class Task_PersonalAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "title",
        "todo",
        "date_field",
        "is_completed",
    )
