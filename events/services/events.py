from ..models import Event
from typing import List


class EventsService:

    @classmethod
    def get_all(cls) -> List[Event]:
        events = Event.objects.order_by('-date')
        for event in events:
            event.image = str(event.image)[7:]
        return events


