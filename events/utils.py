from django.utils import timezone

from fullcalendar.models import CalendarEvent


def get_upcoming_events():
    try:
        now = timezone.datetime.now()
        cutoff = timezone.datetime.today() + timezone.timedelta(days=14)
        events = CalendarEvent.objects.filter(start__lt=cutoff)
        return events
    except:
        return CalendarEvent.objects.none()

    