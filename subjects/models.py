from django.db import models
from common.models import CommonModel


class Subject(CommonModel):

    """ Subject Categories """

    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.subject}: {self.title}"

    class Meta:
        verbose_name_plural = "Subejcts"
