from django.db import models
from common.models import CommonModel


class Content(CommonModel):

    """ Model Definition for Contents """

    class TypeChoices(models.TextChoices):
        BOOK = ("book", "Book")
        LECTURE = ("lecture", "Lecture")

    name = models.CharField(max_length=140,)
    image = models.ImageField(blank=True,)
    types = models.CharField(max_length=8, choices=TypeChoices.choices,)
    description = models.TextField(blank=True,)
    author = models.CharField(max_length=140,)
    company = models.CharField(max_length=140,)
    target_url = models.CharField(max_length=150, default="",)
    leader = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="contents",
    )
    tracks = models.ManyToManyField(
        "contents.Track",
        blank=True,
        related_name="contents",
    )
    books = models.ManyToManyField(
        "contents.Book",
        blank=True,
        related_name="contents",
    )
    lectures = models.ManyToManyField(
        "contents.Lecture",
        blank=True,
        related_name="contents",
    )
    category = models.ManyToManyField(
        "categories.Category",
        blank=True,
        related_name="contents",
    )

    def __str__(self):
        return self.name

    def total_tracks(self):
        return self.tracks.count()

    def rating(content):
        count = content.reviews.count()
        if count == 0:
            return "No Reviews"
        else:
            total_rating = 0
            for review in content.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)


class Track(CommonModel):

    """ Model Definition for Tracks """

    name = models.CharField(max_length=140)
    image = models.ImageField(blank=True,)
    description = models.TextField(blank=True)
    followers_num = models.PositiveIntegerField()
    leader = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="tracks",
    )
    category = models.ManyToManyField(
        "categories.Category",
        blank=True,
        related_name="tracks",
    )

    def __str__(self):
        return self.name

    def rating(track):
        count = track.reviews.count()
        if count == 0:
            return "No Reviews"
        else:
            total_rating = 0
            for review in track.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)


class Book(CommonModel):

    """ Model Definition for Books """

    vesrion = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    sub_title = models.CharField(max_length=140)
    author = models.CharField(max_length=140)
    image = models.ImageField(blank=True,)
    isbn = models.CharField(max_length=140)
    company = models.CharField(max_length=140)

    def __str__(self):
        return self.title


class Lecture(CommonModel):

    """ Model Definition for Lectures """

    vesrion = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    sub_title = models.CharField(max_length=140)
    author = models.CharField(max_length=140)
    image = models.ImageField(blank=True,)
    company = models.CharField(max_length=140)
    books = models.ManyToManyField(
        "contents.Book",
        blank=True,
        related_name="books",
    )

    def __str__(self):
        return self.title
