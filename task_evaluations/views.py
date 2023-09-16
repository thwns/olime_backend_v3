from rest_framework import viewsets
from .models import TaskEvaluation
from .serializers import TaskEvaluationSerializer


class TaskEvaluationViewSet(viewsets.ModelViewSet):
    queryset = TaskEvaluation.objects.all()
    serializer_class = TaskEvaluationSerializer
