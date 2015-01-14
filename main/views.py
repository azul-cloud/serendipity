from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView

from products.models import Product


class HomeListView(ListView):
    model = Product
    template_name = "maincontent/home.html"

    def get_context_data(self, **kwargs):
        # only return the active products
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['product_list'] = Product.active_objects.all()[:3]
        return context


class AboutTemplateView(TemplateView):
    template_name = "maincontent/about.html"    


class ContactTemplateView(TemplateView):
    template_name = "maincontent/contact.html"