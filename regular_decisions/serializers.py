from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Regular_Decision
from subjects.serializers import SubjectSerializer


class Regular_DecisionDetailSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Regular_Decision
        fields = "__all__"


"""class SubjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = (
            "pk",
            "name",
            "ranges",
            "learning_time",
            "guideline",
            "references",
        )"""
