from django.db import models
from django.utils import timezone
import time


class Movie(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    poster = models.TextField(default=None)
    release_time = models.DateTimeField(default=timezone.now())
    # Release time

    # This returns the title of the movie instead of object no
    def __str__(self):
        return self.title


class Ticket(models.Model):
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    booking_time = time.time()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=1)
    expired = models.BooleanField(default=False)

    # movie_time

    # This returns the title of the movie instead of object no
    def __str__(self):
        return f"{self.username} - {self.movie}"
