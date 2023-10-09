from rest_framework import serializers
from .models import Performance
from users.models import User


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'

'''from rest_framework import serializers
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
        )'''
