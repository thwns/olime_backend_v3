from django.contrib import admin
from .models import Loving


@admin.register(Loving)
class Loving(admin.ModelAdmin):
    list_display = (
        "user",
    )
