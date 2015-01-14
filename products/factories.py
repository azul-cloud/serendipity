from factory.django import DjangoModelFactory

from .models import Product, Perk, Ingredient


class IngredientFactory(DjangoModelFactory):
    class Meta:
        model = Ingredient

    name = "Soy"


class PerkFactory(DjangoModelFactory):
    class Meta:
        model = Perk

    name = "No MSG"


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    title = "Bacon Baked Potato"
    description = "This is a mix with bacon"
    type = "MIX"
    price = 8.95
