# Generated by Django 4.0.10 on 2023-10-10 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workbooks', '0002_remove_workbook_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='workbook',
            name='learning_type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='workbook',
            name='subject',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]