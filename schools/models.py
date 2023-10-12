from django.db import models
from common.models import CommonModel


class School(CommonModel):

    """ School Categories """

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.school}: {self.name}"

    class Meta:
        verbose_name_plural = "Schools"
