# Generated by Django 3.1 on 2020-08-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0003_remove_movie_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.TextField(default=None),
        ),
    ]