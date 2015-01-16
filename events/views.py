from django.shortcuts import render, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from braces.views import StaffuserRequiredMixin
from fullcalendar.utils import calendar_options, events_to_json

from .utils import get_upcoming_events, OPTIONS
from .forms import EventCreateForm, EventUpdateForm
from .models import Event

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
    events = Event.objects.all()
    return HttpResponse(events_to_json(events), content_type='application/json')


class EventAdminListView(StaffuserRequiredMixin, ListView):
    model = Event
    template_name = "eventcontent/all.html"


class EventCreateView(StaffuserRequiredMixin, CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = "eventcontent/create.html"


class EventUpdateView(StaffuserRequiredMixin, UpdateView):
    model = Event
    form_class = EventUpdateForm
    template_name = "eventcontent/update.html"

