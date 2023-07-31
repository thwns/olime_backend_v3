from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Current_School
from schools.serializers import SchoolSerializer


class Current_SchoolDetailSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)
    school = SchoolSerializer(read_only=True)

    class Meta:
        model = Current_School
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
