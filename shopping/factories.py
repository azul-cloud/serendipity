from factory.django import DjangoModelFactory

from .models import Sale, SaleProduct, SaleError


class SaleFactory(DjangoModelFactory):
    class Meta:
        model = Sale

    total = "102.00"
    email = "test@gmail.com"
    status = "O"


class SaleProductFactory(DjangoModelFactory):
    # needs product, sale, price
    class Meta:
        model = SaleProduct

    quantity = 1


class SaleErrorFactory(DjangoModelFactory):
    # optionally pass in sale
    class Meta:
        model = SaleError

    location = "C"
    message = "This is a test Card Error"
    problem = "Testing is addictive"


