from django.core.urlresolvers import reverse

from fullcalendar.models import CalendarEvent

class Event(CalendarEvent):
    # extend the CalendarEvent class to add new functionality
    def get_update_url(self):
        return reverse('events_update', kwargs={'pk':self.id})

    def get_absolute_url(self):
        return reverse('events_calendar')

    class Meta:
        proxy = True