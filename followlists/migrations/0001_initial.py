# Generated by Django 4.1.4 on 2023-01-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Followlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('tasks', models.ManyToManyField(to='tasks.task')),
                ('tracks', models.ManyToManyField(to='contents.track')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
