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
    def test_product_type(self):
        url = reverse(self.prefix + 'calendar',)
        response = self.app.get(url)

        assert self.event.title in response

