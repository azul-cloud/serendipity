from django.contrib import admin

from .models import Product, Ingredient, Perk, Type


product_models = [Product, Ingredient, Perk, Type]
admin.site.register(product_models)