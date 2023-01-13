from django.db import models
from common.models import CommonModel


class Following(CommonModel):

    """ Following Model definition """

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="followings",
    )
    track = models.ForeignKey(
        "contents.Track",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="followings",
    )

    def __str__(self):
        return f"{self.kind.title()} booking for: {self.user}"
