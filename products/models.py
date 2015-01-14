from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify

from main.models import SaveSlug


class Ingredient(models.Model):
    # items that the product contains such as dairy, soy
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Perk(models.Model):
    # Products will have certain perks such as No MSG, Gluten Free
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(SaveSlug):
    # These are the products that are sold by Serendipity
    PRODUCT_TYPE_CHOICES = (
        ('MIX', 'Dip Mix'),
        ('RUB', 'Dry Rub'),
        ('MAR', 'Marinade'),
    )

    description = models.CharField(max_length=1024)
    type = models.CharField(max_length=3, choices=PRODUCT_TYPE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    contains = models.ManyToManyField(Ingredient, null=True, blank=True)
    perks = models.ManyToManyField(Perk, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('product_update', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('product_delete', kwargs={'slug':self.slug})
