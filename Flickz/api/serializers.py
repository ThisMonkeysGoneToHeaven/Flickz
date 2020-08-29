from rest_framework import serializers
from moviez.models import Movie, Ticket


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["title", "price", "poster"]


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["username", "phone", "booking_time"]  # movie_time
