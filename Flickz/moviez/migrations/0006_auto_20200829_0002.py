# Generated by Django 3.1 on 2020-08-28 18:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0005_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='booking_time',
            field=models.TimeField(default=datetime.datetime(2020, 8, 28, 18, 32, 33, 659013, tzinfo=utc)),
        ),
    ]