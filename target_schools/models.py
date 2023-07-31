from django.db import models


class Target_School(models.Model):

    """ Target_School Model Definition"""

    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.CASCADE,
        related_name="target_schools",
    )
    school = models.ForeignKey(
        "schools.School",
        on_delete=models.CASCADE,
        related_name='target_schools'
    )

    def __str__(self):
        return self.user
