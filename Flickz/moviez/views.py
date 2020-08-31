from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Ticket
from django.template import loader


def IndexView(request):
    # All movie objects
    movies = Movie.objects.all()
    # the template
    template = "moviez/index.html"
    # the dictionary which has movies variables and will be used in the html file
    context = {"movies": movies}
    return render(request, template, context)


def TicketView(request, slug):
    template = "moviez/detail.html"
    ticket = Ticket.objects.get(id=slug)
    context = {"ticket": ticket}
    return render(request, template, context)


def TicketListView(request):
    template = "moviez/all_tickets.html"
    tickets = Ticket.objects.all()
    context = {"tickets": tickets}
    return render(request, template, context)
