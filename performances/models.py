from django.db import models
from common.models import CommonModel


class Performance(CommonModel):

    # Model for Performance

    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
        related_name="performances",
    )
    subject = models.CharField(max_length=30)
    score = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.name
