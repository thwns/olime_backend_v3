from rest_framework import serializers
from difficult_questions.serializers import Difficult_QuestionSerializer
from .models import Task_Day


class Task_DaySerializer(serializers.ModelSerializer):

    difficult_questions = Difficult_QuestionSerializer(
        many=True,
        # read_only=True,
        required=False,
    )

    class Meta:
        model = Task_Day
        fields = (
            "pk",
            "subject",
            "title",
            "to_do",
            "is_completed",
            "time_taken",
            "date",
            "difficulty",
            "difficult_questions",
        )
