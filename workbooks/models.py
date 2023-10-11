from django.db import models
from common.models import CommonModel


class Workbook(CommonModel):

    """ Workbook Model definition """

    '''user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
        related_name="workbooks",
    )'''
    subject = models.CharField(
        max_length=50,
        blank=True,
    )
    learning_type = models.CharField(
        max_length=50,
        blank=True,
    )
    name = models.CharField(
        max_length=150,
    )
    isbn = models.CharField(
        max_length=150,
        blank=True,
    )
    image_url = models.CharField(
        max_length=150,
        blank=True,
    )
    workbook_evalution = models.ManyToManyField(
        "workbook_evaluations.Workbook_Evaluation",
        blank=True,
        related_name="workbooks",
    )

    def __str__(self):
        return f"{self.name} workbook for: {self.user}"
