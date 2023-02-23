from rest_framework import serializers
from contents.serializers import TrackListSerializer, ContentListSerializer
from reviews.serializers import ReviewSerializer
from replys.serializers import ReplySerializer
from .models import Loving


class LovingSerializer(serializers.ModelSerializer):

    tracks = TrackListSerializer(
        many=True,
        read_only=True,
    )
    contents = ContentListSerializer(
        many=True,
        read_only=True,
    )
    reviews = ReviewSerializer(
        many=True,
        read_only=True,
    )
    replys = ReplySerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Loving
        fields = (
            "pk",
            "name",
            "tracks",
            "contents",
            "reviews",
            "replys",
        )
