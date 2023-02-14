# Generated by Django 4.0.8 on 2023-02-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_review_rating_1_review_rating_2_review_rating_3_and_more'),
        ('lovings', '0002_rename_track_loving_tracks_remove_loving_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loving',
            name='reviews',
            field=models.ManyToManyField(related_name='lovings', to='reviews.review'),
        ),
    ]