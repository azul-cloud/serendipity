# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class CalendarEvent(models.Model):
    """The event set a record for an 
    activity that will be scheduled at a 
    specified date and time. 
    
    It could be on a date and time 
    to start and end, but can also be all day.
    
    :param title: Title of event
    :type title: str.
    
    :param start: Start date of event
    :type start: datetime.
    
    :param end: End date of event
    :type end: datetime.
    
    :param all_day: Define event for all day
    :type all_day: bool.
    """
    title = models.CharField(_('Title'), blank=True, max_length=200)
    start = models.DateTimeField(_('Start'))
    end = models.DateTimeField(_('End'))
    all_day = models.BooleanField(_('All day'), default=False)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return self.title