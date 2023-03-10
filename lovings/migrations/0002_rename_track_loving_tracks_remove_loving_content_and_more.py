# Generated by Django 4.0.8 on 2023-01-31 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0005_remove_track_followers_num'),
        ('lovings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loving',
            old_name='track',
            new_name='tracks',
        ),
        migrations.RemoveField(
            model_name='loving',
            name='content',
        ),
        migrations.AddField(
            model_name='loving',
            name='contents',
            field=models.ManyToManyField(related_name='lovings', to='contents.content'),
        ),
    ]
