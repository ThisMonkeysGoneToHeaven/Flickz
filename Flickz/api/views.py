# Importing from Django Rest Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Importing Models
from moviez.models import Movie, Ticket, Timing

# Importing Serializers
from .serializers import MovieSerializer, TicketSerializerRead, TicketSerializerCreate, TimingSerializer

# Importing time
import time

# Importing from Django
from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


# TICKET

# To get information aboout a particular ticket
@api_view(
    [
        "GET",
    ]
)
def api_detail_ticket(request, slug):
    ticket_expire()  # Checking if any ticket expired
    try:
        ticket = Ticket.objects.get(id=slug)  # getting the ticket through the tickrt id
    except Ticket.DoesNotExist:
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )  # if not exists, will return an error

    if request.method == "GET":
        serializer = TicketSerializerRead(ticket)  # will serialize the data
        return Response(serializer.data)  # returning response


# To get info about all tickets --> Need to use REST to use this
@api_view(
    [
        "GET",
    ]
)
@csrf_exempt
def api_detail_ticket_all(request):
    ticket_expire()  # Checking if any ticket expired

    tickets = Ticket.objects.all()  # getting all tickets

    if request.method == "GET":
        tickets_json = serializers.serialize("json", tickets)  # changing data into json
        return HttpResponse(
            tickets_json, content_type="application/json"
        )  # returning response in json

@csrf_exempt
def api_detail_movie_all(request):
    movies = Movie.objects.all()  # getting all tickets

    if request.method == "GET":
        movies_json = serializers.serialize("json", movies)  # changing data into json
        return HttpResponse(
            movies_json, content_type="application/json"
        )  # returning response in json


# FOR PUT REQUEST (UPDATING)
@api_view(
    [
        "PUT",
    ]
)
def api_update_ticket(request, slug):
    try:
        ticket = Ticket.objects.get(id=slug)  # getting ticket
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # if not found --> error

    if request.method == "PUT":
        serializer = TicketSerializerCreate(
            ticket, data=request.data
        )  # serializigng data
        data = {}
        if serializer.is_valid():  # checking if data is valid
            serializer.save()  # saving to database
            data["success"] = "update successfully"
            return Response(
                data=data, status=status.HTTP_200_OK)  # returning json successful message if everything is successful
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # returning error if data isn't valid


# FOR DELETE REQUEST
@api_view(
    [
        "DELETE",
    ]
)
def api_delete_ticket(request, slug):
    try:
        ticket = Ticket.objects.get(id=slug)  # getting ticket
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # if not found -->  error
    data = {}
    if request.method == "DELETE":
        operation = ticket.delete()  # trying to delete the ticket
        # returning response based on what happens
        if operation:
            data["success"] = "delete successful"
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            data["failure"] = "delete failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)



# FOR POST REQUEST (CREATING)
@api_view(
    [
        "POST",
    ]
)

# FOR POST REQUEST (CREATING)
@api_view(
    [
        "POST",
    ]
)


# FOR POST REQUEST (CREATING)
@api_view(
    [
        "POST",
    ]
)
def api_create_ticket_fine(request):
    tickets = Ticket.objects.all()
    timings = Timing.objects.all()
    ticket = Ticket()  # Creating ticket
    if request.method == "POST":
        the_time = request.data["timing"]  # getting which timing has been requested

        count = 0  # counting how many times that timing had been used
        for tickety in tickets:
            if tickety.timing == Timing.objects.filter(id=the_time)[0]:
                count += 1
        if count > 20:  # if more than 20 --> error
            # already 20 tickets have been booked
            data = {}
            data[
                "Failed"
            ] = "All tickets for this timing has already been booked. Please try another time."
            return Response(data=data, status=status.HTTP_226_IM_USED)
        else:
            serializer = TicketSerializerCreate(
                ticket, data=request.data
            )  # getting the data in serialized form
            if serializer.is_valid():  # checking if data is valid
                serializer.save()  # saving if valid
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )  # returning error if data isn't valid


# FOR POST REQUEST (CREATING)
@api_view(
    [
        "POST",
    ]
)
def api_create_ticket(request):
    tickets = Ticket.objects.all()
    timings = Timing.objects.all()
    ticket = Ticket()  # Creating ticket
    if request.method == "POST":
        the_time = request.data["timing"]  # getting which timing has been requested

        count = 0  # counting how many times that timing had been used
        for tickety in tickets:
            if tickety.timing == Timing.objects.filter(id=the_time)[0]:
                count += 1
        if count > 20:  # if more than 20 --> error
            # already 20 tickets have been booked
            data = {}
            data[
                "Failed"
            ] = "All tickets for this timing has already been booked. Please try another time."
            return Response(data=data, status=status.HTTP_226_IM_USED)
        else:
            serializer = TicketSerializerCreate(
            ticket, data=request.data)# getting the data in serialized form
            if serializer.is_valid():  # checking if data is valid
                serializer.save()  # saving if valid
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )  # returning error if data isn't valid


@api_view(
    [
        "POST",
    ]
)
def api_create_ticket_works(request):
    ticket = Ticket()  # Creating Movie object
    if request.method == "POST":
        serializer = TicketSerializerCreate(
            ticket, data=request.data
        )  # getting the data in serialized form
        if serializer.is_valid():  # checking if data is valid
            serializer.save()  # saving if valid
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # returning error if data isn't valid


# ALL TICKETS OF PARTICULAR TIME
@api_view(
    [
        "GET",
    ]
)
def api_detail_ticket_time(request, slug):
    ticket_expire()  # Checking if any ticket expired
    try:
        tickets = Ticket.objects.filter(timing=slug)  # filtering tickets
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)  # doesn't exist --> errors

    if request.method == "GET":
        tickets_json = serializers.serialize("json", tickets)  # serializing data
        return HttpResponse(
            tickets_json, content_type="application/json"
        )  # returning response in json


# Checking if any ticket has been expired
def ticket_expire():
    tickets = Ticket.objects.all()  # getting all tickets
    for ticket in tickets:
        now = time.time()  # getting the time as of now
        if int(now) - int(ticket.booking_time) > (60 * 60 * 8):  # 8 HOURS
            print(f"Deleting {ticket}")
            ticket.delete()  # Deleting ticket


# All operations for Movie model


@api_view(
    [
        "GET",
    ]
)
def api_detail_movie(request, slug):
    try:
        movie = Movie.objects.get(id=slug)  # getting movie
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # if not found --> error

    if request.method == "GET":
        serializer = MovieSerializer(movie)  # serializing data
        return Response(serializer.data)  # return response


# FOR POST REQUEST (CREATING)
@api_view(
    [
        "POST",
    ]
)
def api_create_movie(request):
    movie = Movie()  # Creating Movie object
    if request.method == "POST":
        serializer = MovieSerializer(
            movie, data=request.data
        )  # getting the data in serialized form
        if serializer.is_valid():  # checking if data is valid
            serializer.save()  # saving if valid
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # returning error if data isn't valid


# FOR PUT REQUEST
@api_view(
    [
        "PUT",
    ]
)
def api_update_movie(request, slug):
    try:
        movie = Movie.objects.get(id=slug)  # getting movie
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # if not found --> error

    if request.method == "PUT":
        serializer = MovieSerializer(
            movie, data=request.data
        )  # getting the data from user in serialized form
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "updated successfully"  # returning successful response
            return Response(data=data)
        return Response(
            serializer.errors, status.HTTP_400_BAD_REQUEST
        )  # if data isn't valid returning error


# FOR DELETE REQUEST
@api_view(
    [
        "DELETE",
    ]
)
def api_delete_movie(request, slug):
    try:
        movie = Movie.objects.get(id=slug)  # getting movie
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # if not found --> error
    data = {}
    if request.method == "DELETE":
        # returning repsonse on basis of what happens here
        operation = movie.delete()
        if operation:
            data["success"] = "delete successful"  # returning successful response
            print("Deleted Successfully")
        else:
            # returning errors
            data["failure"] = "delete failed"
        return Response(data=data)



# TIMING
# FOR DELETE REQUEST
@api_view(
    [
        "POST",
    ]
)
def api_create_timing(request):
    time = Timing()  # Creating Movie object
    if request.method == "POST":
        serializer = TimingSerializer(
            time, data=request.data
        )  # getting the data in serialized form
        if serializer.is_valid():  # checking if data is valid
            serializer.save()  # saving if valid
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )  # returning error if data isn't valid