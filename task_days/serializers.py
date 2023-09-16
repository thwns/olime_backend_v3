from rest_framework import serializers
from .models import Task_Day
from users.models import User


class Task_DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_Day
        fields = '__all__'

    def create(self, validated_data):
        users_data = validated_data.pop('user')
        task_day = Task_Day.objects.create(**validated_data)
        for user_data in users_data:
            task_day.user.add(user_data)
        return task_day

    def update(self, instance, validated_data):
        users_data = validated_data.pop('user')
        instance.subject = validated_data.get('subject', instance.subject)
        instance.title = validated_data.get('title', instance.title)
        instance.to_do = validated_data.get('to_do', instance.to_do)

        instance.user.clear()
        for user_data in users_data:
            instance.user.add(user_data)

        instance.save()
        return instance
