from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.template import loader

# Create your views here.


def IndexView(request):
    # All movie objects
    movies = Movie.objects.all()
    # the template
    template = "moviez/index.html"
    # the dictionary which has movies variables and will be used in the html file
    context = {"movies": movies}
    return render(request, template, context)


def TicketView(request, slug):
    return HttpResponse("Details for movie id: " + str(slug))