from django.db import models
from common.models import CommonModel


class Reply(CommonModel):

    """Reply from a User to a Review"""

    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
        related_name="replys",
    )
    review = models.ForeignKey(
        "reviews.Review",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="replys",
    )
    payload = models.TextField(blank=True,)
    rating = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}⭐️"

    def lovers_num(reply):
        count = reply.lovings.count()
        return count
