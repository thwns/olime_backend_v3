from django.contrib import admin
from .models import Early_Decision


@admin.register(Early_Decision)
class Early_DecisionAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "subject",
    )
    search_fields = (
        "user",
    )

    # ^ : startswith
    # = : exact
