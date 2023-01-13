from django.db import models
from common.models import CommonModel


class Followlist(CommonModel):

    """ FollowList Model Definition """
    name = models.CharField(
        max_length=150,
    )
    tracks = models.ManyToManyField(
        "contents.Track",
        related_name="followlists",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="followlists",
    )
    tasks = models.ManyToManyField(
        "tasks.Task",
        related_name="followlists",
    )

    def __str__(self):
        return self.name
