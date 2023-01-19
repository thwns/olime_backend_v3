from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Task
from contents.serializers import TrackSerializer


class TaskDetailSerializer(serializers.ModelSerializer):

    leader = TinyUserSerializer(read_only=True)
    track = TrackSerializer(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            "pk",
            "name",
            "ranges",
            "learning_time",
            "guideline",
            "references",
        )
