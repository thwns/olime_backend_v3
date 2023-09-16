from rest_framework import serializers
from .models import Difficult_Question


class Difficult_QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Difficult_Question
        fields = ("id", "user", "name")
        read_only_fields = ('id',)
        extra_kwargs = {
            'name': {'required': False},
            'user': {'required': False}
        }
