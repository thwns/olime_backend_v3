from rest_framework import serializers
from .models import TaskEvaluation
from difficult_questions.models import Difficult_Question
from difficult_questions.serializers import Difficult_QuestionSerializer
from .models import TaskEvaluation


class TaskEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskEvaluation
        fields = '__all__'

    def create(self, validated_data):
        difficult_questions_data = validated_data.pop('difficult_question')
        task_evaluation = TaskEvaluation.objects.create(**validated_data)
        for dq_data in difficult_questions_data:
            task_evaluation.difficult_question.add(dq_data)
        return task_evaluation

    def update(self, instance, validated_data):
        difficult_questions_data = validated_data.pop('difficult_question')
        instance.task_day = validated_data.get('task_day', instance.task_day)
        instance.user = validated_data.get('user', instance.user)
        instance.is_completed = validated_data.get(
            'is_completed', instance.is_completed)
        instance.time_taken = validated_data.get(
            'time_taken', instance.time_taken)
        instance.date = validated_data.get('date', instance.date)
        instance.difficulty = validated_data.get(
            'difficulty', instance.difficulty)

        instance.difficult_question.clear()
        for dq_data in difficult_questions_data:
            instance.difficult_question.add(dq_data)

        instance.save()
        return instance
