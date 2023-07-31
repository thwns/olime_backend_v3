from rest_framework.viewsets import ModelViewSet
from .models import Subject
from .serializers import SubjectSerializer


class SubjectViewSet(ModelViewSet):

    serializer_class = SubjectSerializer
