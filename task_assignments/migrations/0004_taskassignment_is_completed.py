# Generated by Django 4.0.10 on 2023-10-10 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_assignments', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskassignment',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
