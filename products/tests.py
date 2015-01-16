from django.core.urlresolvers import reverse
from django.test import TestCase

from django_webtest import WebTest

from .models import Product, Type
from .factories import ProductFactory, TypeFactory
from main.factories import NormalUserFactory, StaffUserFactory


class ProductSetUp(TestCase):
    def setUp(self):
        self.user = NormalUserFactory.create()
        self.staff = StaffUserFactory.create()
        self.type = TypeFactory.create()
        self.product = ProductFactory.create(title="Product Test Product")
        self.mix_product = ProductFactory.create(
            title="Mix Test Product", 
            type=self.type
        )

        self.prefix = "product_"

    def access_test(self, url, text):
        '''
        test access of a view. We'll test against an anon user, normal user,
        and a staff user
        '''
        anon_response = self.app.get(url)
        user_response = self.app.get(url, user=self.user)
        response = self.app.get(url, user=self.staff)

        assert anon_response.status_code == 302
        assert text not in user_response
        assert text in response


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
        response = self.app.get(url)

    def test_product_type(self):
        url = reverse(self.prefix + 'type', kwargs={'slug':self.type.slug})
        response = self.app.get(url, user=self.user)

        assert self.mix_product.title in response
        assert self.product.title not in response

    def test_product_detail(self):
        url = self.product.get_absolute_url()
        response = self.app.get(url)

        assert self.product.title in response

    def test_product_admin_home(self):
        url = reverse(self.prefix + 'admin_home')
        self.access_test(url, self.product.title)

    def test_product_create(self):
        url = reverse(self.prefix + 'create')
        self.access_test(url, "Create New Product")

    def test_product_update(self):
        url = self.product.get_update_url()
        self.access_test(url, "Update Product")


class ProductFormTest(ProductSetUp, WebTest):
    def test_product_create_form(self):
        url = reverse(self.prefix + 'create')

        form = self.app.get(url, user=self.staff).form
        form['title'] = 'My Test Mix'
        form['description'] = 'The Test Description'
        form['type'] = '1'
        form['price'] = '5.95'

        response = form.submit().follow()

        # make sure the response has the newly created post
        assert form['title'].value in response

    def test_product_update_form(self):
        url = self.product.get_update_url()

        form = self.app.get(url, user=self.staff).form
        form['title'] = 'Edited Test Mix'
        form['description'] = 'The Test Description'
        form['type'] = '1'
        form['price'] = '5.95'

        response = form.submit().follow()

        # make sure the response has the updated form
        assert form['title'].value in response
        assert self.product.title not in response
    

