from django.contrib import admin
from .models import Task_Day
from users.models import User


@admin.register(Task_Day)
class Task_DayAdmin(admin.ModelAdmin):
    list_display = ("subject", "title", "to_do", "get_users",)

    def get_users(self, obj):
        return ", ".join([str(user) for user in obj.user.all()])
    get_users.short_description = "Users"
