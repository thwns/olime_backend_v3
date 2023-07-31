from django.db import models


class Early_Decision(models.Model):

    """ Early_Decision Model Definition"""

    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.CASCADE,
        related_name="early_decisions",
    )
    subject = models.ForeignKey(
        "subjects.Subject",
        on_delete=models.CASCADE,
        related_name='early_decisions'
    )

    def __str__(self):
        return self.user
