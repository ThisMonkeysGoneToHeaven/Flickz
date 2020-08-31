from django.contrib import admin
from .models import Movie, Ticket, Timing

# Register your models here.

admin.site.register(Movie)
admin.site.register(Ticket)
admin.site.register(Timing)
