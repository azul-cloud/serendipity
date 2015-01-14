from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product
from .forms import ProductCreateForm, ProductUpdateForm


class ProductHomeListView(ListView):
    model = Product
    template_name = "productcontent/home.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "productcontent/detail.html"


class ProductAdminTemplateView(TemplateView):
    template_name = "productcontent/admin.html"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "productcontent/create.html"


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = "productcontent/update.html"


class ProductDeleteView(DeleteView):
    model = Product
