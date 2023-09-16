from django.contrib import admin
from .models import TaskEvaluation


@admin.register(TaskEvaluation)
class TaskEvaluationAdmin(admin.ModelAdmin):
    list_display = ("task_day", "user", "is_completed", "time_taken",
                    "date", "difficulty", "get_difficult_questions")

    def get_difficult_questions(self, obj):
        return ", ".join([str(dq) for dq in obj.difficult_question.all()])
    get_difficult_questions.short_description = "Difficult Questions"
