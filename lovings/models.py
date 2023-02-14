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
    contents = models.ManyToManyField(
        "contents.Content",
        related_name="lovings",
        blank=True,
    )
    tracks = models.ManyToManyField(
        "contents.Track",
        related_name="lovings",
        blank=True,
    )
    reviews = models.ManyToManyField(
        "reviews.Review",
        related_name="lovings",
        blank=True,
    )
    '''replys = models.ManyToManyField(
        "replys.Reply",
        related_name="lovings",
    )'''

    def __str__(self):
        return f"{self.name} loving for: {self.user}"
