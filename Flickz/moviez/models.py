from django.db import models
from django.utils import timezone
import time
import json
import datetime

# This is the Timing model which has all the shows timing
class Timing(models.Model):
    time = models.CharField(max_length=250)

    def __str__(self):
        return self.time


class Movie(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    poster = models.TextField()
    # This returns the title of the movie instead of object no
    def __str__(self):
        return self.title


class Ticket(models.Model):
    username = models.CharField(max_length=50)
    phone = models.IntegerField()
    booked_date = models.DateField(
        max_length=250,
        default=datetime.datetime.now().strftime("%Y-%m-%d"),
        editable=False,
    )
    booked_time = models.TimeField(
        max_length=250,
        default=datetime.datetime.now().strftime("%H:%M:%S"),
        editable=False,
    )
    booking_time = models.IntegerField(default=int(time.time()), editable=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    timing = models.ForeignKey(Timing, on_delete=models.CASCADE)  # movie_time

    # This returns the title of the movie instead of object no
    def __str__(self):
        return f"{self.username} - {self.movie}"
