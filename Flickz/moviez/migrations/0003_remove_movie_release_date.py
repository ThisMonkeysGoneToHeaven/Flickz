# Generated by Django 3.1 on 2020-08-28 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0002_auto_20200828_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='release_date',
        ),
    ]