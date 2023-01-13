from django.contrib import admin
from .models import Following


@admin.register(Following)
class Following(admin.ModelAdmin):
    list_display = (
        "user",
        "track",
    )
