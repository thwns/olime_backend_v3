# Generated by Django 4.0.10 on 2023-09-16 14:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task_days', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task_day',
            name='user',
            field=models.ManyToManyField(null=True, related_name='task_days', to=settings.AUTH_USER_MODEL),
        ),
    ]
