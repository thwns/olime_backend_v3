from django.db import models
from common.models import CommonModel


class Following(CommonModel):

    """ Following Model definition """

    name = models.CharField(
        max_length=150,
        null=True,
    )
    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.CASCADE,
        related_name="followings",
    )
    tracks = models.ManyToManyField(
        "contents.Track",
        related_name="followings",
    )

    def __str__(self):
        return f"{self.name} following for: {self.user}"
