from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from carton.cart import Cart
from products.models import Product


class AddView(TemplateView):
    def get(self, request, *args, **kwargs):
        cart = Cart(request.session)
        product = Product.objects.get(id=kwargs["pk"])
        cart.add(product, price=product.price)
        return HttpResponse("Added")


class RemoveView(TemplateView):
    def get(self, request, *args, **kwargs):
        cart = Cart(request.session)
        product = Product.objects.get(id=kwargs["pk"])
        cart.remove(product)
        return HttpResponse("Removed")


class CartTemplateView(TemplateView):
    template_name = "shoppingcontent/cart.html"