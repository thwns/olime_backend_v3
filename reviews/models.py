from django.db import models
from common.models import CommonModel


class Review(CommonModel):

    """Review from a User to a Content or Track or Task"""

    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
        related_name="reviews",
    )
    content = models.ForeignKey(
        "contents.Content",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    track = models.ForeignKey(
        "contents.Track",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    task = models.ForeignKey(
        "tasks.Task",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    kind = models.CharField(max_length=30,)
    payload = models.TextField(blank=True,)
    rating = models.PositiveIntegerField()
    rating_1 = models.PositiveIntegerField(null=True)
    rating_2 = models.PositiveIntegerField(null=True)
    rating_3 = models.PositiveIntegerField(null=True)
    rating_4 = models.PositiveIntegerField(null=True)
    rating_5 = models.PositiveIntegerField(null=True)

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}⭐️"
