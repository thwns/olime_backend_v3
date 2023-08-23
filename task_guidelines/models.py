from django.db import models
from common.models import CommonModel


class Task_Day(CommonModel):

    """ Task_Day Model definition """

    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
        related_name="task_maths",
    )
    subject = models.CharField(
        max_length=150,
    )
    title = models.CharField(
        max_length=150,
    )
    to_do = models.CharField(
        max_length=150,
    )
    is_completed = models.BooleanField(
        default=False
    )
    time_taken = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    date = models.DateTimeField()
    difficulty = models.models.IntegerField()
    difficult_question = models.ForeignKey(
        "difficult_questions.Difficult_Question",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="task_maths",
    )

    def __str__(self):
        return f"{self.name} task_day for: {self.user}"
