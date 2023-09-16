from rest_framework import serializers
from .models import TaskAssignment
from users.models import User


class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignment
        fields = '__all__'
