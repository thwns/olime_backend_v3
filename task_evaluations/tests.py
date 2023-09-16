from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from .models import TaskEvaluation


class TaskEvaluationTests(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser2', password='testpassword2')

        # Create test Task_Day object
        self.task_day = Task_Day.objects.create(
            subject='Test Subject for Evaluation',
            title='Test Title for Evaluation',
            to_do='Test To Do for Evaluation'
        )
        self.task_day.user.add(self.user)

        # Create test TaskEvaluation object
        self.task_evaluation = TaskEvaluation.objects.create(
            task_day=self.task_day,
            user=self.user,
            is_completed=True,
            time_taken=120.50,
            date="2023-09-16T10:20:30Z",
            difficulty=3
        )
