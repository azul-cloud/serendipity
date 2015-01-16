from django.conf.urls import patterns, include, url

from . import views


prefix = "events_"

urlpatterns = patterns('',
    url(r'admin/create/$', views.EventCreateView.as_view(), name=prefix + "create"),
    # url(r'admin/update/(?P<slug>\S+)/$', views.ProductUpdateView.as_view(), 
    #     name=prefix + "update"),
    url(r'admin/$', views.EventAdminListView.as_view(), name=prefix + "admin_home"),

    url(r'all/$', views.all_events, name=prefix + "all"),
    url(r'$', views.CalendarTemplateView.as_view(), name=prefix + "calendar"),
)
