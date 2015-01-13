from django.shortcuts import render
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = "maincontent/home.html"


class AboutTemplateView(TemplateView):
    template_name = "maincontent/about.html"    


class ContactTemplateView(TemplateView):
    template_name = "maincontent/contact.html"