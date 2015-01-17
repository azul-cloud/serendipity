from django.core.urlresolvers import reverse
from django.test import TestCase

from django_webtest import WebTest

from products.factories import ProductFactory


class ShoppingSetUp(TestCase):
    def setUp(self):
        self.product1 = ProductFactory.create(title="First Product")
        self.product2 = ProductFactory.create(title="Second Product")

        self.prefix = "shopping_"


class ShoppingViewTest(ShoppingSetUp, WebTest):
    def test_add_item(self):
        url1 = reverse(self.prefix + 'add', kwargs={'pk':self.product1.id})
        url2 = reverse(self.prefix + 'add', kwargs={'pk':self.product2.id})
        response1 = self.app.get(url1)
        response2 = self.app.get(url2)

        assert "Added" in response1
        assert "Added" in response2

    def test_remove_item(self):
        url = reverse(self.prefix + 'remove', kwargs={'pk':self.product2.id})
        response = self.app.get(url)

        assert "Removed" in response

    def test_cart(self):
        url = reverse(self.prefix + 'cart')
        response = self.app.get(url)

        assert response.status_code == 200
    

