from rest_framework import serializers
from contents.serializers import TrackListSerializer
from .models import Following


class FollowingSerializer(serializers.ModelSerializer):

    tracks = TrackListSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Following
        fields = (
            "pk",
            "name",
            "tracks",
        )
