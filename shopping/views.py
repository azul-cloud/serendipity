import stripe 
import json

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from carton.cart import Cart

from .models import Sale, SaleProduct, SaleError
from products.models import Product


class AddView(TemplateView):
    def get(self, request, *args, **kwargs):
        cart = Cart(request.session)
        product = Product.objects.get(id=kwargs["pk"])
        cart.add(product, price=product.price)
        return HttpResponse("Added")


class RemoveSingleView(TemplateView):
    def get(self, request, *args, **kwargs):
        cart = Cart(request.session)
        product = Product.objects.get(id=kwargs["pk"])
        cart.remove_single(product)
        return HttpResponse("Removed Single " + str(product))


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
        context['cart_stripe_total'] = int(Cart(self.request.session).total * 100)
        return context


class SaleDetailView(DetailView):
    template_name = "shoppingcontent/sale.html"
    model = Sale


class SaleListView(ListView):
    template_name = "shoppingcontent/sales_list.html"
    model = Sale

class SaleErrorListView(ListView):
    template_name = "shoppingcontent/sales_error_list.html"
    model = SaleError


def charge(request):
    ''' This function is split into 4 separate parts, which are all wrapped around a try:
        except block.

        The first part is where we charge the card through Stripe. Stripe will either 
        accept the payment or send back various different error messages depending on
        what went wrong.

        The second thing we do is very simple, empty the user's cart. 

        The third thing is that we're going to create a Sale object for our own records.
        This is where we'll see what items have been sold, and also manage orders.

        The last thing is creating the sale items, which is really part of creating the
        sale, but it is separated in a different try block so that we are sure to create
        the sale item if something goes wrong when creating the items associated with the
        sale.

        Each try block will writhe to the SaleError model if something goes wrong.
    '''
    if request.method == "POST":
        stripe.api_key = settings.STRIPE_SECRET_KEY
        email = request.POST['stripeEmail']
        stripe_amount = request.POST['stripeAmount']
        sale_products_string = request.POST['products']

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
          charge = stripe.Charge.create(
              amount=stripe_amount, # amount in cents, again
              currency="usd",
              card=request.POST['stripeToken'],
              description=email
          )
        except stripe.CardError as e:
            # The card has been declined
            text = "There was an error processing your card, and we were not able to charge. "
            return render(request, "shoppingcontent/error.html", 
                {'text': text, 'error': e})
        except stripe.InvalidRequestError as e:
            # Attempt to use the token multiple times.
            text = "Your order has already been processed, and it can only be processed once. " \
                   "If you refreshed this page, that is why you're seeing this error."
            return render(request, "shoppingcontent/error.html", 
                {'text': text})
        except stripe.APIConnectionError as e:
            # Connection error with Stripe
            text = "There was a connection error with our payment processor. Please try again in a few minutes, your cart should still be intact."
            return render(request, "shoppingcontent/error.html", 
                {'text': text, 'error': e})
        finally:
            # write to the error log if needed
            try:
                SaleError.objects.create(message=e, location="C")
            except:
                pass

        try:
            # clear the cart. If there is an error just keep going.
            cart = Cart(request.session).clear()
        except Exception as e:
            SaleError.objects.create(message=e, location="A")
            pass

        try:
            # create the sale object
            if "test" in stripe.api_key:
                live = False
            elif "live" in stripe.api_key:
                live = True

            sale = Sale.objects.create(live=live, email=email, total="%.2f" % (int(stripe_amount) / 100))
        except Exception as e:
            SaleError.objects.create(message=e, location="S", problem="email -" + email + ", amount - " + amount)
            text = "Sorry, there was an error processing your order. You have been billed, and " + \
                   "we have general information about your order, but will be contacting you to get the details."

            return render(request, "shoppingcontent/error.html", 
                {'text': text})

        try:
            # create the product sales objects
            obj = json.loads(sale_products_string)
            for i in obj:
                id = i.get('id')
                quantity = i.get('quantity')
                product = Product.objects.get(id=id)
                SaleProduct.objects.create(
                    product=product, 
                    quantity=quantity,
                    price=product.price,
                    sale=sale
                )
            return render(request, "shoppingcontent/success.html", 
                {'sale': sale, 'email': email})
        except Exception as e:
            SaleError.objects.create(message=e, location="I", problem=sale_products_string, sale=sale)
            text = "There was a problem processing your purchase. The charge went through successfully, " + \
                   "and we have recorded the sale. However, the product details we will need to contact you about. " + \
                   "Sorry for the inconvenience."
            return render(request, "shoppingcontent/error.html", 
                {'text': text})
    else:
        text = "Error: This page is only meant to be hit by the server after a payment."
        return render(request, "shoppingcontent/error.html", 
                {'text': text})



