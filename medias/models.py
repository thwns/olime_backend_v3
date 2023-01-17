from django.db import models
from common.models import CommonModel


class Photo(CommonModel):

    file = models.URLField()
    description = models.CharField(
        max_length=140,
    )
    content = models.ForeignKey(
        "contents.Content",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    track = models.ForeignKey(
        "contensts.Track",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    book = models.ForeignKey(
        "contensts.Book",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    lecture = models.ForeignKey(
        "contensts.Lecture",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "Photo File"


class Video(CommonModel):

    file = models.URLField()
    content = models.OneToOneField(
        "contents.Content",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Video File"
