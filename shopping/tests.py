from django.core.urlresolvers import reverse
from django.test import TestCase

from django_webtest import WebTest

from .factories import SaleFactory, SaleProductFactory, SaleErrorFactory
from products.factories import ProductFactory


class ShoppingSetUp(TestCase):
    def setUp(self):
        self.product1 = ProductFactory.create(title="First Product")
        self.product2 = ProductFactory.create(title="Second Product")

        self.sale = SaleFactory.create()
        self.product_sale1 = SaleProductFactory.create(
            sale=self.sale, 
            product=self.product1,
            price=8.50
        )
        self.product_sale2 = SaleProductFactory.create(
            sale=self.sale,
            product=self.product1, 
            quantity=2,
            price=5.95
        )

        self.error1 = SaleErrorFactory.create()
        self.error2 = SaleErrorFactory.create(sale=self.sale)

        self.prefix = "shopping_"


class ShoppingViewTest(ShoppingSetUp, WebTest):
    ''' the cart tests in the ShoppingViewTest class are just testing against 
        the URL and not actually going through the user motions, that part is 
        done in the ShoppingFunctionTest class
    '''
    def test_add_item(self):
        url1 = reverse(self.prefix + 'add', kwargs={'pk':self.product1.id})
        url2 = reverse(self.prefix + 'add', kwargs={'pk':self.product2.id})
        response1 = self.app.get(url1)
        response2 = self.app.get(url2)

        assert "Added" in response1
        assert "Added" in response2

    def test_remove_single_item(self):
        url = reverse(self.prefix + 'remove_single', kwargs={'pk':self.product2.id})
        response = self.app.get(url)

        assert "Removed Single" in response

    def test_remove_item(self):
        url = reverse(self.prefix + 'remove', kwargs={'pk':self.product2.id})
        response = self.app.get(url)

        assert "Removed" in response

    def test_cart(self):
        url = reverse(self.prefix + 'cart')
        response = self.app.get(url)

        assert response.status_code == 200

    def test_sales_list(self):
        url = reverse('shopping_sales')
        response = self.app.get(url)

        # Don't know why, but in the test it is stripping the decimal values?
        assert "$102" in response

    def test_sale_detail(self):
        url = self.sale.get_absolute_url()
        response = self.app.get(url)

        assert self.sale.email in response

    def test_sale_error_list(self):
        url = reverse(self.prefix + 'sale_errors')
        response = self.app.get(url)

        assert self.error1.message in response
    

class ShoppingFunctionTest(ShoppingSetUp, WebTest):
    def test_add_item(self):
        ''' in this test we will need to click on the element and make sure the
            item was added and the button was changed correctly according to
            script.js
        '''
        pass

    def test_increment_item(self):
        # In the cart click the button that increments the item in the cart.
        pass

    def test_decrement_item(self):
        # In the cart click the button that decrements the item in the cart.
        pass

    def test_remove_item(self):
        # In the cart click the button that removes the item from the cart
        pass

