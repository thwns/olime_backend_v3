from rest_framework import serializers
from .models import Task_Personal


class Task_PersonalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task_Personal
        fields = (
            "pk",
            "user",
            "title",
            "todo",
            "date_field",
            "is_completed",
        )
