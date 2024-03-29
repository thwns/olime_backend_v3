from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Kr")
        EN = ("en", "En")

    login_path = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    avatar = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=150, default="",)
    is_host = models.BooleanField(default=False,)
    gender = models.CharField(
        max_length=10, choices=GenderChoices.choices, null=True)
    language = models.CharField(
        max_length=2, choices=LanguageChoices.choices, null=True)
    grade = models.CharField(max_length=20, blank=True) # 자기 학년
    current_school = models.CharField(max_length=50, blank=True) # 자기 학교
    target_school = models.CharField(max_length=50, blank=True)
