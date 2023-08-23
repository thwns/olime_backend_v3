from django.contrib import admin
from .models import Task_Day


@admin.register(Task_Day)
class Task_Day(admin.ModelAdmin):
    list_display = (
        "user",
    )
