from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "kind_major",
        "kind_minor",
    )
    list_filter = (
        "kind_major",
    )
