from django.contrib import admin
from .models import Current_School


@admin.register(Current_School)
class Current_SchoolAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "school",
    )
    search_fields = (
        "user",
    )

    # ^ : startswith
    # = : exact
