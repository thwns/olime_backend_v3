from django.contrib import admin
from .models import Target_School


@admin.register(Target_School)
class Target_SchoolAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "school",
    )
    search_fields = (
        "user",
    )

    # ^ : startswith
    # = : exact
