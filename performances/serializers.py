from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Performance


class PerformanceSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Performance
        fields = (
            "pk",
            "user",
            "subject",
            "score",
            "created_at",
            "updated_at",
        )
