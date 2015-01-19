from django.db import models
from django.core.urlresolvers import reverse

from main.models import TimeStampedModel
from products.models import Product


class Sale(TimeStampedModel):
    # record the details of a sale
    STATUS_CHOICES = (
        ('O', 'Ordered'),
        ('S', 'Sent'),
    )
    total = models.DecimalField(decimal_places=2, max_digits=6)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="O")
    live = models.NullBooleanField()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.created) + ' - ' + self.email

    def get_absolute_url(self):
        return reverse('shopping_sale', kwargs={'pk':self.id})


class SaleError(TimeStampedModel):
    ERROR_CHOICES = (
        ('C', 'Card'),
        ('A', 'Cart'),
        ('S', 'Sale'),
        ('I', 'Items'),
    )
    sale = models.ForeignKey(Sale, null=True)
    location = models.CharField(max_length="1", choices=ERROR_CHOICES)
    message = models.CharField(max_length="500")
    problem = models.CharField(max_length="500")

    class Meta:
        ordering = ['-created']


class SaleProduct(models.Model):
    # this model will keep track of how many of each product was sold
    sale = models.ForeignKey(Sale)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.product.title