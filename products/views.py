from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product, Type
from .forms import ProductCreateForm, ProductUpdateForm


class ProductListView(ListView):
    model = Product
    template_name = "productcontent/products.html"

    def get_context_data(self, **kwargs):
        # only return the active products
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['product_list'] = Product.active_objects.all()
        return context


class ProductTypeDetailView(DetailView):
    model = Type
    template_name = "productcontent/products.html"

    def get_context_data(self, **kwargs):
        # get the active products for the selected type
        context = super(ProductTypeDetailView, self).get_context_data(**kwargs)
        context['product_list'] = Product.active_objects.filter(type=self.get_object())
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "productcontent/detail.html"


class ProductAdminListView(ListView):
    model = Product
    template_name = "productcontent/all.html"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = "productcontent/create.html"


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = "productcontent/update.html"
