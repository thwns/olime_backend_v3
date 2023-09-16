from rest_framework import serializers
from .models import Task_Day
from users.models import User


class Task_DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_Day
        fields = '__all__'
