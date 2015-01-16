from django.utils import timezone

from factory.django import DjangoModelFactory

from .models import Event


class EventFactory(DjangoModelFactory):
    class Meta:
        model = Event

    title = "Test Title"
    description = "This is the event description"
    location = "1035 Fake st., Kirkland, WA"
    start = timezone.datetime.now() + timezone.timedelta(hours=2)
    end = start + timezone.timedelta(hours=2)

    
