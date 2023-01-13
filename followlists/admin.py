from django.contrib import admin
from .models import Followlist


@admin.register(Followlist)
class FollowlistAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
        "created_at",
        "updated_at",
    )
