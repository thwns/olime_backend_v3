from django.db import models
from common.models import CommonModel


class Loving(CommonModel):

    """ Loving Model definition """

    name = models.CharField(
        max_length=150,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="lovings",
    )
    content = models.ManyToManyField(
        "contents.Content",
        related_name="lovings",
    )
    track = models.ManyToManyField(
        "contents.Track",
        related_name="lovings",
    )

    def __str__(self):
        return f"{self.name} loving for: {self.user}"
