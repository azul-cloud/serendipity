from django.core.urlresolvers import reverse
from django.utils import timezone
from django.test import TestCase

from django_webtest import WebTest

from .utils import get_upcoming_events
from .factories import EventFactory


class EventSetUp(TestCase):
    def setUp(self):
        self.event = EventFactory.create()
        self.far_event = EventFactory.create(start=timezone.datetime.now() + timezone.timedelta(days=15))

        self.prefix = "events_"


class EventUtilTest(EventSetUp):
    def test_upcoming(self):
        # get the upcoming events
        events = get_upcoming_events()
        
        assert self.event in events
        assert self.far_event not in events


class EventViewTest(EventSetUp, WebTest):
    def test_calendar(self):
        url = reverse(self.prefix + 'calendar',)
        response = self.app.get(url)

        assert self.event.title in response

    def test_event_admin_home(self):
        url = reverse(self.prefix + 'admin_home')
        response = self.app.get(url)

        assert self.event.title in response

    def test_event_create(self):
        url = reverse(self.prefix + 'create')
        response = self.app.get(url)

        assert "Create New Event" in response

    def test_event_update(self):
        url = self.event.get_update_url()
        response = self.app.get(url)

        assert "Update Event" in response


class EventFormTest(EventSetUp, WebTest):
    def test_event_create_form(self):
        url = reverse(self.prefix + 'create')

        form = self.app.get(url).form
        form['title'] = 'My Test Event'
        form['start'] = '2015-01-25 10:00'
        form['end'] = '2015-01-25 14:00'

        response = form.submit().follow()

        # make sure the response has the newly created post
        assert 'My Test Event' in response

    def test_event_update_form(self):
        url = self.event.get_update_url()

        form = self.app.get(url).form
        form['title'] = 'Edited Test Event'
        form['start'] = '2015-01-25 10:00'
        form['end'] = '2015-01-25 14:00'

        response = form.submit().follow()

        # make sure the response has the updated form
        assert 'Edited Test Event' in response
        assert self.event.title not in response

