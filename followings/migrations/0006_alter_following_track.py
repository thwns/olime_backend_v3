# Generated by Django 4.1.4 on 2023-01-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_book_unique_id_lecture_unique_id'),
        ('followings', '0005_remove_following_track_alter_following_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='following',
            name='track',
            field=models.ManyToManyField(related_name='followings', to='contents.track'),
        ),
    ]
