# Generated by Django 4.0.10 on 2023-09-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task_Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('todo', models.CharField(max_length=150)),
                ('date_field', models.JSONField()),
                ('is_completed', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]