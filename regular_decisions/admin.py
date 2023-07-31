from django.contrib import admin
from .models import Regular_Decision


@admin.register(Regular_Decision)
class Regular_DecisionAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "subject",
    )
    search_fields = (
        "user",
    )

    # ^ : startswith
    # = : exact
