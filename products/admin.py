from django.contrib import admin

from .models import Product, Ingredient, Perk


product_models = [Product, Ingredient, Perk]
admin.site.register(product_models)