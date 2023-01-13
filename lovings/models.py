from django.db import models
from common.models import CommonModel


class Loving(CommonModel):

    """ Loving Model definition """

    class LovingKindChoices(models.TextChoices):
        CONTENTS = "content", "Content"
        TRACKS = "track", "Track"

    kind = models.CharField(
        max_length=15,
        choices=LovingKindChoices.choices,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="lovings",
    )
    content = models.ForeignKey(
        "contents.Content",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="lovings",
    )
    track = models.ForeignKey(
        "contents.Track",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="lovings",
    )

    def __str__(self):
        return f"{self.kind.title()} loving for: {self.user}"
