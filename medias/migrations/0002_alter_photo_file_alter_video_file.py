# Generated by Django 4.0.8 on 2023-02-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]