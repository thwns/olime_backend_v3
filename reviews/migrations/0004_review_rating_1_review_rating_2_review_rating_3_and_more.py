# Generated by Django 4.0.8 on 2023-02-07 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_content_alter_review_task_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating_1',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='rating_2',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='rating_3',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='rating_4',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='rating_5',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
