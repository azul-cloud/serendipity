from django.core.urlresolvers import reverse
from django.test import TestCase

from django_webtest import WebTest

from .models import Product, Type
from .factories import ProductFactory, TypeFactory
from main.factories import NormalUserFactory, AdminUserFactory


class ProductSetUp(TestCase):
    def setUp(self):
        self.user = NormalUserFactory.create()
        self.type = TypeFactory.create()
        self.product = ProductFactory.create(title="Product Test Product")
        self.mix_product = ProductFactory.create(
            title="Mix Test Product", 
            type=self.type
        )

        self.prefix = "product_"


class ProductModelTest(ProductSetUp):
    def test_model(self):
        product = Product.objects.get(title=self.product.title)
        self.assertNotEqual(product.slug, None)

    def test_type(self):
        type = Type.objects.get(title=self.type.title)
        assert type.slug is not None


class ProductViewTest(ProductSetUp, WebTest):
    def test_product_all(self):
        url = reverse(self.prefix + 'home')
        response = self.app.get(url, user=self.user)

    def test_product_type(self):
        url = reverse(self.prefix + 'type', kwargs={'slug':self.type.slug})
        response = self.app.get(url, user=self.user)

        assert self.mix_product.title in response
        assert self.product.title not in response

    def test_product_detail(self):
        url = self.product.get_absolute_url()
        response = self.app.get(url, user=self.user)

        assert self.product.title in response

    def test_admin_home(self):
        url = reverse(self.prefix + 'admin_home')
        response = self.app.get(url, user=self.user)

        assert self.product.title in response

    def test_product_create(self):
        url = reverse(self.prefix + 'create')
        response = self.app.get(url, user=self.user)

        assert "Create New Product" in response

    def test_product_update(self):
        url = self.product.get_update_url()
        response = self.app.get(url, user=self.user)

        assert "Update Product" in response


class ProductFormTest(ProductSetUp, WebTest):
    def test_product_create_form(self):
        url = reverse(self.prefix + 'create')

        form = self.app.get(url).form
        form['title'] = 'My Test Mix'
        form['description'] = 'The Test Description'
        form['type'] = '1'
        form['price'] = '5.95'

        response = form.submit().follow()

        # make sure the response has the newly created post
        assert 'My Test Mix' in response

    def test_product_update_form(self):
        url = self.product.get_update_url()

        form = self.app.get(url).form
        form['title'] = 'Edited Test Mix'
        form['description'] = 'The Test Description'
        form['type'] = '1'
        form['price'] = '5.95'

        response = form.submit().follow()

        # make sure the response has the updated form
        assert 'Edited Test Mix' in response
        assert self.product.title not in response
    

