from rest_framework import serializers
from workbook_evaluations.serializers import Workbook_EvaluationSerializer
from .models import Workbook


class WorkbookSerializer(serializers.ModelSerializer):

    workbook_evaluations = Workbook_EvaluationSerializer(
        many=True,
        # read_only=True,
        required=False,
    )

    class Meta:
        model = Workbook
        fields = (
            "pk",
            "name",
            "isbn",
            "workbook_evaluations",
        )
