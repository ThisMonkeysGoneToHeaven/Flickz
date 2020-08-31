from django.urls import path
from .views import IndexView, TicketListView, TicketView

app_name = "moviez"

urlpatterns = [
    path("", IndexView, name="Index"),
    path("ticket/<int:slug>/", TicketView, name="ticket-detail"),
    path("tickets/", TicketListView, name="all-tickets"),
]
