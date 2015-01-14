from django import forms
from django.forms import ModelForm

from .models import Product

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder, Field, Button


product_fields = ['title', 'description', 'type', 'price', 'contains', 'perks']

class ProductCreateForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Product
        fields = product_fields

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '<h1>Create New Product</h1>',
                Div('title', css_class="col-sm-12"),
                Div('description', css_class="col-sm-12"),
                Div('type', css_class="col-sm-6"),
                Div('price', css_class="col-sm-6"),
                Div('contains', css_class="col-sm-6"),
                Div('perks', css_class="col-sm-6"),
            ),
            ButtonHolder(
                Submit('submit', 'Create New Item', css_class='btn-lg'),
                css_class = "text-center"                
            ),
        )


class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = product_fields

    def __init__(self, *args, **kwargs):
        super(ProductUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()