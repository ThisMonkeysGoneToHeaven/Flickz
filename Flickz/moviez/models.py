from django.db import models
import datetime

from django.utils import timezone

now = timezone.now()


class Movie(models.Model):
    title = models.TextField()
    price = models.IntegerField()
    poster = models.TextField(default=None)


class Ticket(models.Model):
    username = models.TextField()
    phone = models.IntegerField()
    booking_time = models.TimeField(default=now)
    # movie_time
