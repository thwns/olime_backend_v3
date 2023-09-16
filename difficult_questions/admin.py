from django.contrib import admin
from .models import Difficult_Question


@admin.register(Difficult_Question)
class Difficult_Question(admin.ModelAdmin):
    list_display = (
        "user",
    )
