# Generated by Django 3.1 on 2020-08-31 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviez', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='booked_time',
            field=models.TimeField(default='11:37:59', editable=False, max_length=250),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='booking_time',
            field=models.IntegerField(default=1598854079, editable=False),
        ),
    ]