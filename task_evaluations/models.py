from django.db import models
from common.models import CommonModel


class TaskEvaluation(CommonModel):
    """ TaskEvaluation Model definition """

    task_day = models.ForeignKey(
        "task_days.Task_Day",
        null=True,
        on_delete=models.SET_NULL,
        related_name="task_evaluations",
    )
    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
        related_name="task_evaluations",
    )
    is_completed = models.BooleanField(
        default=False
    )
    time_taken = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    date = models.DateTimeField()
    difficulty = models.IntegerField(
        null=True,
        blank=True,
    )
    difficult_question = models.ManyToManyField(
        "difficult_questions.Difficult_Question",
        related_name="task_evaluations",
        blank=True,
    )

    def __str__(self):
        return f"{self.task_day} task evaluation for: {self.user}"
