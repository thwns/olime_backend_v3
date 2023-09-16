from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from .models import Task_Day


class TaskDayTests(APITestCase):

    def setUp(self):
        # 테스트용 유저 생성
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

        # 테스트용 Task_Day 객체 생성
        self.task_day = Task_Day.objects.create(
            subject='Test Subject',
            title='Test Title',
            to_do='Test To Do'
        )
        self.task_day.user.add(self.user)

    def test_create_task_day(self):
        url = reverse('taskday-list')
        data = {
            'subject': 'Test Subject 2',
            'title': 'Test Title 2',
            'to_do': 'Test To Do 2',
            'user': [self.user.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task_Day.objects.count(), 2)
        self.assertEqual(Task_Day.objects.get(id=2).subject, 'Test Subject 2')

    def test_get_task_day_list(self):
        url = reverse('taskday-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_task_day(self):
        url = reverse('taskday-detail', args=[self.task_day.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['subject'], 'Test Subject')

    def test_update_task_day(self):
        url = reverse('taskday-detail', args=[self.task_day.id])
        data = {
            'subject': 'Updated Subject',
            'title': 'Updated Title',
            'to_do': 'Updated To Do',
            'user': [self.user.id]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task_Day.objects.get(
            id=self.task_day.id).subject, 'Updated Subject')

    def test_delete_task_day(self):
        url = reverse('taskday-detail', args=[self.task_day.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task_Day.objects.count(), 0)
