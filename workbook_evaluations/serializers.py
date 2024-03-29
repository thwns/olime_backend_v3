'''from rest_framework import serializers
from users.serializers import TinyUserSerializer
from .models import Workbook_Evaluation


class Workbook_EvaluationSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Workbook_Evaluation
        fields = (
            "pk",
            "user",
            "workbook",
            "evaluation_item",
            "star_point",
            "created_at",
            "updated_at",
        )'''
from rest_framework import serializers
from .models import Workbook_Evaluation
from users.models import User


class Workbook_EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workbook_Evaluation
        fields = '__all__'
