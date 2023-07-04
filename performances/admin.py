from django.contrib import admin
from .models import Performance


class WordFilter(admin.SimpleListFilter):

    title = "Filter by words!"

    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, performances):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            performances


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "subject",
        "score",
    )
    list_filter = (
        WordFilter,
        "subject",
        "user__is_host",
    )
