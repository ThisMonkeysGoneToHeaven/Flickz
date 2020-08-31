from rest_framework import serializers
from moviez.models import Movie, Ticket, Timing


# For Movie Model
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["title", "price", "poster"]


# For ticket model (For Reading only)
class TicketSerializerRead(serializers.ModelSerializer):
    movie = serializers.CharField(source="movie.title", read_only=True)
    timing = serializers.CharField(source="timing.time", read_only=True)

    class Meta:
        model = Ticket
        fields = [
            "id",
            "username",
            "phone",
            "movie",
            "booked_date",
            "booked_time",
            "timing",
        ]


# For ticket model (for creating)
class TicketSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            "id",
            "username",
            "phone",
            "movie",
            "booked_date",
            "booked_time",
            "timing",
        ]  # movie_time


# For Movie Model
class TimingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timing
        fields = ["time"]