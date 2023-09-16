from django.contrib import admin
from .models import TaskGuideline


@admin.register(TaskGuideline)
class TaskGuideline(admin.ModelAdmin):
    list_display = ()
