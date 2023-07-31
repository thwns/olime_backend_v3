from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Early_Decision
from subjects.serializers import SubjectSerializer


class Early_DecisionDetailSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)
    subject = SubjectSerializer(read_only=True)

    class Meta:
        model = Early_Decision
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
