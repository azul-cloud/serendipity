import stripe 

from django.conf import settings
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

    def get_context_data(self, **kwargs):
        # only return the active products
        context = super(CartTemplateView, self).get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context


def charge(request):
    ''' We need to do two things here. First of all we need to create the charge in Stripe.
        After the charge has registered successfully, we need to create the Sale object
        so we know what was sold
    '''
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get the credit card details submitted by the form
    token = request.POST['stripeToken']

    # Create the charge on Stripe's servers - this will charge the user's card
    try:
      charge = stripe.Charge.create(
          amount=1000, # amount in cents, again
          currency="usd",
          card=token,
          description=request.POST['stripeEmail']
      )
      return HttpResponse("Charge successful!")
    except stripe.CardError as e:
      # The card has been declined
      return HttpResponse("There was a card error: " + e)


    # TODO: Save the Sale Object


