from django.db import models
from django.contrib.auth.models import User
from common.models import CommonModel


class Difficult_Question(CommonModel):
    """ Difficult_Question Model Definition """

    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
        related_name="difficult_questions",)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
