from rest_framework import serializers
from difficult_questions.serializers import Difficult_QuestionSerializer
from .models import TaskGuideline


class TaskGuidelineSerializer(serializers.ModelSerializer):
    average_time_taken = serializers.FloatField(read_only=True)
    difficulty_count = serializers.JSONField(read_only=True)
    top_difficult_questions = serializers.JSONField(read_only=True)

    class Meta:
        model = TaskGuideline
        fields = (
            "id",
            "task_day",
            "average_time_taken",
            "difficulty_count",
            "top_difficult_questions",
        )
