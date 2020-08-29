from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from moviez.models import Movie, Ticket
from .serializers import MovieSerializer, TicketSerializer


@api_view(
    [
        "GET",
    ]
)
def api_detail_ticket(request, slug):

    try:
        ticket = Ticket.objects.get(id=slug)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)
