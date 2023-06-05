from django.db import models
from common.models import CommonModel


class Content(CommonModel):

    """ Model Definition for Contents """

    class TypeChoices(models.TextChoices):
        BOOK = ("book", "Book")
        LECTURE = ("lecture", "Lecture")

    content_parent = models.CharField(max_length=140, null=True,)
    # 만일 책 이름이 쎈 고등수학(상), 쎈 고등수학(하)라면 이를 좀합해서 부르는 쎈
    name = models.CharField(max_length=140,)
    types = models.CharField(max_length=8, choices=TypeChoices.choices,)
    image = models.URLField(blank=True, null=True,)
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
            return 0
        else:
            total_rating = 0
            for review in content.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)

    def rating(content):
        count = content.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in content.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)

    def rating_1(content):
        count = content.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in content.reviews.all().values("rating_1"):
                total_rating += review["rating_1"]
            return round(total_rating / count, 2)

    def rating_2(content):
        count = content.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in content.reviews.all().values("rating_2"):
                total_rating += review["rating_2"]
            return round(total_rating / count, 2)

    def rating_3(content):
        count = content.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in content.reviews.all().values("rating_3"):
                total_rating += review["rating_3"]
            return round(total_rating / count, 2)

    def rating_4(content):
        count = content.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in content.reviews.all().values("rating_4"):
                total_rating += review["rating_4"]
            return round(total_rating / count, 2)

    def rating_5(content):
        count = content.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in content.reviews.all().values("rating_5"):
                total_rating += review["rating_5"]
            return round(total_rating / count, 2)

    def lovers_num(content):
        count = content.lovings.count()
        return count


class Track(CommonModel):

    """ Model Definition for Tracks """

    name = models.CharField(max_length=140)
    image = models.URLField(blank=True, null=True,)
    description = models.TextField(blank=True)
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
            return 0
        else:
            total_rating = 0
            for review in track.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)

    def followers_num(track):
        count = track.followings.count()
        return count

    def lovers_num(track):
        count = track.lovings.count()
        return count


class Book(CommonModel):

    """ Model Definition for Books """

    unique_id = models.PositiveIntegerField(null=True,)
    vesrion = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    sub_title = models.CharField(max_length=140)
    author = models.CharField(max_length=140)
    image = models.URLField(blank=True, null=True,)
    isbn = models.CharField(max_length=140)
    company = models.CharField(max_length=140)

    def __str__(self):
        return self.title


class Lecture(CommonModel):

    """ Model Definition for Lectures """

    unique_id = models.PositiveIntegerField(null=True,)
    vesrion = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    sub_title = models.CharField(max_length=140)
    author = models.CharField(max_length=140)
    image = models.URLField(blank=True, null=True,)
    company = models.CharField(max_length=140)
    books = models.ManyToManyField(
        "contents.Book",
        blank=True,
        related_name="books",
    )

    def __str__(self):
        return self.title
