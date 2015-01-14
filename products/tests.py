from django.core.urlresolvers import reverse
from django.test import TestCase

from django_webtest import WebTest

from .models import Product
from .factories import ProductFactory
from main.factories import NormalUserFactory, AdminUserFactory


class ProductSetUp(TestCase):
    def setUp(self):
        self.user = NormalUserFactory.create()
        self.product = ProductFactory.create()
        self.prefix = "product_"


class ProductModelTest(ProductSetUp):
    def test_model(self):
        product = Product.objects.get(title=self.product.title)
        self.assertNotEqual(product.slug, None)


class ProductViewTest(ProductSetUp, WebTest):
    def test_product_home(self):
        url = reverse(self.prefix + 'home')
        response = self.app.get(url, user=self.user)

    def test_product_detail(self):
        url = self.product.get_absolute_url()
        response = self.app.get(url, user=self.user)

    def test_product_create(self):
        url = reverse(self.prefix + 'create')
        response = self.app.get(url, user=self.user)

    def test_product_update(self):
        url = self.product.get_update_url()
        response = self.app.get(url, user=self.user)

    def test_product_delete(self):
        url = self.product.get_delete_url()
        response = self.app.get(url, user=self.user)


class ProductFormTest(ProductSetUp, WebTest):
    def test_product_create_form(self):
        pass

    def test_product_update_form(self):
        pass

    def test_product_delete_form(self):
        pass

        # url = reverse('blog_create')

        # post = {
        #     "title":"Posted Title",
        #     "headline":"My headline",
        #     "body":"<h1>Incoming from test</h1>",
        #     "city":self.city
        # }

        # response = self.app.post(url, post, user=self.user)

        # # make sure the response has the newly created post
        # self.assertEqual(response.status_code, 200)
        # self.assertContains(response, post['title'])
    

