from django.contrib import admin
from .models import Workbook


@admin.register(Workbook)
class Workbook(admin.ModelAdmin):
    list_display = (

    )
