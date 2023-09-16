from django.db import models
from common.models import CommonModel


class Task_Personal(CommonModel):

    """ Task_Personal Model definition """

    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
        related_name="task_personals",
    )
    title = models.CharField(
        max_length=150,
    )
    todo = models.CharField(
        max_length=150,
    )
    date_field = models.JSONField()  # Using JSONField to save list of dates
    is_completed = models.JSONField()

    def __str__(self):
        return f"{self.title} task_personal for: {self.user}"
