from django.contrib import admin
from .models import TaskAssignment
from users.models import User


@admin.register(TaskAssignment)
class TaskAssignmentAdmin(admin.ModelAdmin):
    list_display = ("user", "task_day", "assigned_date",)
