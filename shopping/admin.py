from django.contrib import admin

from .models import Sale, SaleProduct, SaleError


shopping_models = [Sale, SaleProduct, SaleError]
admin.site.register(shopping_models)