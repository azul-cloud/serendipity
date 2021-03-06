import os
from django.core.urlresolvers import reverse
from django.db import models
from django.templatetags.static import static
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


class Type(SaveSlug):
    # categorize products by type such as dip, mix, rub, or marinade
    plural = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('product_type', kwargs={'slug':self.slug})


class AvailableProductManager(models.Manager):
    '''
    manager that will only return active products
    '''
    def get_queryset(self):
        return super(AvailableProductManager, self).get_queryset().filter(available=True)


class Product(SaveSlug):
    # These are the products that are sold by Serendipity
    PRODUCT_TYPE_CHOICES = (
        ('MIX', 'Dip Mix'),
        ('RUB', 'Dry Rub'),
        ('MAR', 'Marinade'),
    )

    def get_picture_path(instance, filename):
        return os.path.join('products/%s' % filename)

    description = models.CharField(max_length=1024)
    type = models.ForeignKey(Type, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    contains = models.ManyToManyField(Ingredient, null=True, blank=True)
    perks = models.ManyToManyField(Perk, null=True, blank=True)
    available = models.BooleanField(default=True)
    picture = models.ImageField(upload_to=get_picture_path, null=True, blank=True)

    active_objects = AvailableProductManager()
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_picture_location(self):
        # for now just have the picture be the default
        if self.picture:
            return self.picture.url
        else:
            return static('img/default.jpeg')

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('product_update', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('product_delete', kwargs={'slug':self.slug})
