from django.conf.urls import patterns, include, url

from . import views


prefix = "events_"

urlpatterns = patterns('',
    url(r'all/$', views.all_events, name=prefix + "all"),
    url(r'$', views.CalendarTemplateView.as_view(), name=prefix + "calendar"),
)
