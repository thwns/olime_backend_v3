from django.contrib import admin
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "description",
    )
    list_filter = (
        "title",
    )
