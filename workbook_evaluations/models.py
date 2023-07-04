from django.db import models
from common.models import CommonModel


class Workbook_Evaluation(CommonModel):

    # Workbook Evaluation

    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
        related_name="workbook_evaluations",
    )
    workbook = models.ManyToManyField(
        "workbooks.Workbook",
        blank=True,
        related_name="workbook_evaluations",
    )
    evaluation_item = models.CharField(max_length=30)
    star_point = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.name
