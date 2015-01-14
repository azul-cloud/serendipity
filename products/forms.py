from django import forms
from django.forms import ModelForm

from .models import Product

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder, Field, Button


product_fields = ['title', 'description', 'type', 'price', 'contains', 'perks']


class ProductBaseForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ProductBaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                self.form_title,
                Div('title', css_class="col-sm-6 col-sm-offset-3"),
                Div('description', css_class="col-sm-12"),
                Div('type', css_class="col-sm-6"),
                Div('price', css_class="col-sm-6"),
                Div('contains', css_class="col-sm-6"),
                Div('perks', css_class="col-sm-6"),
            ),
            ButtonHolder(
                Submit('submit', self.btn_text, css_class='btn-lg'),
                css_class = "text-center",
            ),
        )

    class Meta:
        model = Product
        fields = product_fields


class ProductCreateForm(ProductBaseForm):
    form_title = '<h1>Create New Product</h1>'
    btn_text = 'Create New Item'


class ProductUpdateForm(ProductBaseForm):
    form_title = '<h1>Update Product</h1>'
    btn_text = 'Update Item'


