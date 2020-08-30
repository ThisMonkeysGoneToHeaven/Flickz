from rest_framework import serializers
from moviez.models import Movie, Ticket

# For Movie Model
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["title", "price", "poster"]


# For ticket model
class TicketSerializer(serializers.ModelSerializer):
    movie = serializers.CharField(source="movie.title", read_only=True)

    class Meta:
        model = Ticket
        fields = ["username", "phone", "movie", "booking_time"]  # movie_time
