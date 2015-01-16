from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from . import views


prefix = "main_"

urlpatterns = patterns('',
    url(r'^$', views.HomeListView.as_view(), name=prefix + "home"),
    url(r'^about/$', views.AboutTemplateView.as_view(), name=prefix + "about"),
    url(r'^contact/$', views.ContactTemplateView.as_view(), name=prefix + "contact"),
    url(r'^recipeideas/$', views.RecipeIdeasListView.as_view(), name=prefix + "recipe_ideas"),
    url(r'^robots\.txt', TemplateView.as_view(template_name="maincontent/robots.txt"),
        name = prefix + 'robots'),
)
