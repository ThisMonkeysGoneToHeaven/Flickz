from django.urls import path
from .views import (
    api_detail_ticket,
    api_detail_movie,
    api_update_ticket,
    api_delete_ticket,
    api_create_ticket,
    api_create_movie,
    api_update_movie,
    api_delete_movie,
    api_detail_ticket_all,
    api_detail_ticket_time,
    api_detail_movie_all,
)

app_name = "moviez"

urlpatterns = [
    # TICKET
    # To get detail about particular ticket
    path("ticket/<int:slug>/", api_detail_ticket, name="ticket-detail"),
    # to update particular ticket
    path("ticket/<int:slug>/update", api_update_ticket, name="ticket-update"),
    # to delete particular ticket
    path("ticket/<int:slug>/delete", api_delete_ticket, name="ticket-delete"),
    # to create ticket
    path("ticket/create", api_create_ticket, name="ticket-create"),
    # to get details about all tickets
    path("ticket/all", api_detail_ticket_all, name="ticket-detail-all"),
    # for giving details about tickets on basis of time
    path("ticket/time/<int:slug>/", api_detail_ticket_time, name="ticket-detail-time"),
    # MOVIE
    # to create movie
    path("movie/create", api_create_movie, name="movie-create"),
    # to update movie
    path("movie/<int:slug>/update", api_update_movie, name="movie-update"),
    # to delete movie
    path("movie/<int:slug>/delete", api_delete_movie, name="movie-delete"),
    # to get details about particular movie
    path("movie/<int:slug>/", api_detail_movie, name="movie-detail"),
    # to get details about all movies
    path("movie/all", api_detail_movie_all, name="movie-detail-all"),
]
