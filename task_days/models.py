from django.db import models
from common.models import CommonModel


class Task_Day(CommonModel):
    """ Task_Day Model definition """
    subject = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    to_do = models.CharField(max_length=150)
    user = models.ManyToManyField(
        "users.User", related_name="task_days")

    def __str__(self):
        return self.title
