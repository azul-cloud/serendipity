from django.utils import timezone

from factory.django import DjangoModelFactory

from fullcalendar.models import CalendarEvent


class EventFactory(DjangoModelFactory):
    class Meta:
        model = CalendarEvent

    title = "Test Title"
    description = "This is the event description"
    location = "1035 Fake st., Kirkland, WA"
    start = timezone.datetime.now() + timezone.timedelta(hours=2)
    end = start + timezone.timedelta(hours=2)

    
