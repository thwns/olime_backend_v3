from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from users.models import User
from .models import TaskAssignment


class TaskAssignmentModelTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1", password="password1")
        self.user2 = User.objects.create_user(
            username="user2", password="password2")
        self.task_day = Task_Day.objects.create(
            subject="Test Subject",
            title="Test Title",
            to_do="Test To Do",
        )
        self.task_day.user.add(self.user1, self.user2)
        self.task_assignment = TaskAssignment.objects.create(
            user=self.user1,
            task_day=self.task_day,
            assigned_date="2023-09-15"
        )

    def test_task_assignment_creation(self):
        self.assertEqual(self.task_assignment.user, self.user1)
        self.assertEqual(self.task_assignment.task_day, self.task_day)
        self.assertEqual(str(self.task_assignment.assigned_date), "2023-09-15")

    def test_task_assignment_update(self):
        self.task_assignment.assigned_date = "2023-09-16"
        self.task_assignment.save()
        self.assertEqual(str(self.task_assignment.assigned_date), "2023-09-16")

    def test_task_assignment_delete(self):
        self.task_assignment.delete()
        self.assertEqual(TaskAssignment.objects.count(), 0)


class TaskAssignmentViewTestCase(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1", password="password1")
        self.user2 = User.objects.create_user(
            username="user2", password="password2")
        self.task_day = Task_Day.objects.create(
            subject="Test Subject",
            title="Test Title",
            to_do="Test To Do",
        )
        self.task_day.user.add(self.user1, self.user2)
        self.task_assignment = TaskAssignment.objects.create(
            user=self.user1,
            task_day=self.task_day,
            assigned_date="2023-09-15"
        )

        self.url = reverse('taskassignment-detail',
                           kwargs={'pk': self.task_assignment.pk})
        self.client.login(username="user1", password="password1")

    def test_get_task_assignment(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['assigned_date'], "2023-09-15")

    def test_put_task_assignment(self):
        data = {
            "user": self.user1.pk,
            "task_day": self.task_day.pk,
            "assigned_date": "2023-09-16",
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(TaskAssignment.objects.get(
            pk=self.task_assignment.pk).assigned_date, "2023-09-16")

    def test_delete_task_assignment(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(TaskAssignment.objects.count(), 0)
