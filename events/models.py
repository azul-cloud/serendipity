import datetime

from django.db import models

from django.core.urlresolvers import reverse

from fullcalendar.models import CalendarEvent

class EventManager(models.Manager):
    def upcoming_events(self):
        now = datetime.datetime.now()
        cutoff = datetime.datetime.today() + datetime.timedelta(days=14)
        events = Event.objects.filter(start__lt=cutoff, start__gt=now).order_by('-start')
        return events


class Event(CalendarEvent):
    # extend the CalendarEvent class to add new functionality
    objects = EventManager()

    def get_update_url(self):
        return reverse('events_update', kwargs={'pk':self.id})

    def get_absolute_url(self):
        return reverse('events_calendar')

    class Meta:
        proxy = True