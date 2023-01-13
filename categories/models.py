from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    """ Content or Track Category """

    class CategoryKindMajorChoices(models.TextChoices):
        CONTENTS = ("contents", "Contents")
        TRACKS = ("tracks", "Tracks")

    class CategoryKindMinorChoices(models.TextChoices):
        SUBJECT_MAJORS = ("subject_majors", "Subject_majors")
        SUBJECT_MINORS = ("subject_minors", "Subject_minors")
        TARGET_GRADE = ("target_grades", "Target_grades")
        TARGET_TEST = ("target_tests", "Target_tests")

    name = models.CharField(max_length=50)
    kind_major = models.CharField(
        max_length=15,
        choices=CategoryKindMajorChoices.choices,
    )
    kind_minor = models.CharField(
        max_length=15,
        choices=CategoryKindMinorChoices.choices,
    )

    def __str__(self):
        return f"{self.kind_major}: {self.kind_minor}: {self.name}"

    class Meta:
        verbose_name_plural = "Categories"
