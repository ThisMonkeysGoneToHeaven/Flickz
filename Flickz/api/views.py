from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.utils import timezone
from moviez.models import Movie, Ticket
from .serializers import MovieSerializer, TicketSerializer
import time


from django.http import HttpResponse
from django.core import serializers


# TICKET

# GET request for retrieving information about ticket
@api_view(
    [
        "GET",
    ]
)
def api_detail_ticket(request, slug):
    # ticket_expire()  # Checking if any ticket expired
    try:
        ticket = Ticket.objects.get(id=slug)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)


# FOR ALL TICKETS
@api_view(
    [
        "GET",
    ]
)
def api_detail_ticket_all(request):
    tickets = Ticket.objects.all()

    if request.method == "GET":
        # serializer = TicketSerializer(tickets)
        # return Response(serializer.data)
        tickets_json = serializers.serialize("json", tickets)
        return HttpResponse(tickets_json, content_type="application/json")


# FOR PUT REQUEST (UPDATING)
@api_view(
    [
        "PUT",
    ]
)
def api_update_ticket(request, slug):
    try:
        ticket = Ticket.objects.get(id=slug)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = TicketSerializer(ticket, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successfully"
            return Response(data=data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# FOR DELETE REQUEST
@api_view(
    [
        "DELETE",
    ]
)
def api_delete_ticket(request, slug):
    try:
        ticket = Ticket.objects.get(id=slug)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {}
    if request.method == "DELETE":
        operation = ticket.delete()
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# FOR POST REQUEST (CREATING)
@api_view(
    [
        "POST",
    ]
)
def api_create_ticket(request):

    ticket = Ticket()
    if request.method == "POST":
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)


def ticket_expire(request):
    now = time.time()
    # if now - booking time > 60*60*8:
    # delete

    tickets = Ticket.objects.all()
    for ticket in tickets:
        if now - ticket.booking_time > 60 * 60 * 1:  # 8 HOURS
            ticket.delete()


# MOVIE


@api_view(
    [
        "GET",
    ]
)
def api_detail_movie(request, slug):

    try:
        movie = Movie.objects.get(id=slug)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


# FOR POST REQUEST (CREATING)
@api_view(
    [
        "POST",
    ]
)
def api_create_movie(request):

    movie = Movie()
    if request.method == "POST":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)


# FOR PUT REQUEST
@api_view(
    [
        "PUT",
    ]
)
def api_update_movie(request, slug):
    try:
        movie = Movie.objects.get(id=slug)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = MovieSerializer(movie, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successfully"
            return Response(data=data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# FOR DELETE REQUEST
@api_view(
    [
        "DELETE",
    ]
)
def api_delete_movie(request, slug):
    try:
        movie = Movie.objects.get(id=slug)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {}
    if request.method == "DELETE":
        operation = movie.delete()
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
