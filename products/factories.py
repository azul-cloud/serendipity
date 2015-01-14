from factory.django import DjangoModelFactory

from .models import Product, Perk, Ingredient, Type


class IngredientFactory(DjangoModelFactory):
    class Meta:
        model = Ingredient

    name = "Soy"


class PerkFactory(DjangoModelFactory):
    class Meta:
        model = Perk

    name = "No MSG"


class TypeFactory(DjangoModelFactory):
    class Meta:
        model = Type

    title = "Mix"


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    description = "This is a mix with bacon"
    price = 8.95
