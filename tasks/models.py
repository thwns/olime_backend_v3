from django.db import models


class Task(models.Model):

    """ Task Model Definition"""

    name = models.CharField(max_length=140)
    ranges = models.CharField(max_length=140)
    learning_time = models.DecimalField(max_digits=5, decimal_places=1,)
    guideline = models.TextField(blank=True)
    references = models.CharField(max_length=140, blank=True)
    track = models.ForeignKey(
        "contents.Track",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def rating(task):
        count = task.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in task.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)
