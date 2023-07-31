from django.db import models


class Current_School(models.Model):

    """ Current_School Model Definition"""

    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.CASCADE,
        related_name="current_schools",
    )
    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name='current_schools'
    )

    def __str__(self):
        return self.user
