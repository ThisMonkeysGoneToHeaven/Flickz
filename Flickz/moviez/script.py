from .models import Ticket
import time


def main():
    while True:
        tickets = Ticket.objects.all()
        for ticket in tickets:
            now = time.time()
            if now - ticket.booking_time > 60 * 60 * 1:  # 8 HOURS
                print(f"Deleting {ticket}")
                ticket.delete()
