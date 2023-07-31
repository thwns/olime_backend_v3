from django.db import models


class Regular_Decision(models.Model):

    """ Regular_Decision Model Definition"""

    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.CASCADE,
        related_name="regular_decisions",
    )
    subject = models.ForeignKey(
        "subjects.Subject",
        on_delete=models.CASCADE,
        related_name='regular_decisions'
    )

    def __str__(self):
        return self.user
