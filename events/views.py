from django.shortcuts import render, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView

from fullcalendar.models import CalendarEvent
from fullcalendar.utils import calendar_options, events_to_json
from .utils import get_upcoming_events


OPTIONS = """{  timeFormat: "H:mm",
                header: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'month,agendaWeek,agendaDay',
                },
                allDaySlot: false,
                firstDay: 0,
                weekMode: 'liquid',
                slotMinutes: 15,
                defaultEventMinutes: 30,
                minTime: 8,
                maxTime: 20,
                editable: false,
                dayClick: function(date, allDay, jsEvent, view) {
                    if (allDay) {       
                        $('#calendar').fullCalendar('gotoDate', date)      
                        $('#calendar').fullCalendar('changeView', 'agendaDay')
                    }
                },
                eventClick: function(event, jsEvent, view) {
                    if (view.name == 'month') {     
                        $('#calendar').fullCalendar('gotoDate', event.start)      
                        $('#calendar').fullCalendar('changeView', 'agendaDay')
                    }
                },
            }"""

# Create your views here.
class CalendarTemplateView(TemplateView):
    event_url = '/events/all/'
    template_name = "eventcontent/calendar.html"

    def get_context_data(self, **kwargs):
        context = super(CalendarTemplateView, self).get_context_data(**kwargs)
        context['calendar_config_options'] = calendar_options(self.event_url, OPTIONS)
        context['next_events'] = get_upcoming_events()
        return context



def all_events(request):
    '''
    return all events as a JSON object to pass to calendar
    '''
    events = CalendarEvent.objects.all()
    return HttpResponse(events_to_json(events), content_type='application/json')

