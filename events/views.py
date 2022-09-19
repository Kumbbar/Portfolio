from django.shortcuts import render
from mails.forms import MailForm
from .services.events import EventsService


def get_all_events_page(request):
    form = MailForm()
    events = EventsService.get_all()
    return render(request, 'events.html', {'events': events, 'form': form})

