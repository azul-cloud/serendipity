from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^', include('main.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^events/', include('events.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
