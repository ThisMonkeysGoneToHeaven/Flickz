from django.urls import path
from .views import IndexView, TicketView

app_name = "moviez"

urlpatterns = [
    path("moviez/", IndexView, name="Index"),
    path("movie/<int:slug>/", TicketView, name="ticket-booking"),
]
