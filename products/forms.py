from django import forms
from django.forms import ModelForm

from .models import Product

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder, Field, Button


class ProductCreateForm(ModelForm):
    class Meta:
        model = Product

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()


class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product

    def __init__(self, *args, **kwargs):
        super(ProductUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()