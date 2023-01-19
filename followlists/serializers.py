from rest_framework import serializers
from .models import Followlist
from users.serializers import TinyUserSerializer
from tasks.serializers import TaskListSerializer
from contents.serializers import TrackListSerializer
from contents.models import Track
from tasks.models import Task


class FollowlistDetailSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)
    tasks = TaskListSerializer(
        read_only=True,
        many=True,
    )
    track = TrackListSerializer(
        read_only=True,
    )

    class Meta:
        model = Followlist
        fields = "__all__"


class FollowlistListSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)
    tasks = TaskListSerializer(
        read_only=True,
        many=True,
    )
    track = TrackListSerializer(
        read_only=True,
    )

    class Meta:
        model = Followlist
        fields = (
            "pk",
            "name",
            "user",
            "tasks",
            "track",
        )
