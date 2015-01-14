from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from django_webtest import WebTest

from .models import User
from .factories import NormalUserFactory, StaffUserFactory
from products.factories import ProductFactory


class MainSetUp(TestCase):
    def setUp(self):
        self.user = NormalUserFactory.create()
        self.staff = StaffUserFactory.create()
        self.product = ProductFactory.create(title="Main Test Product")


class MainModelTest(MainSetUp):

    def test_model(self):
        # instance = Model.objects.get(name = "Tag 1")
        # self.assertNotEqual(instance.slug, None)
        pass


class MainViewTest(MainSetUp, WebTest):
    def setUp(self):
        MainModelTest.setUp(self)

    def test_home(self):
        url = reverse('main_home')
        response = self.app.get(url, user=self.user)

        assert self.product.title in response

    def test_product_admin(self):
        url = reverse('main_home')
        anon_response = self.app.get(url)
        user_response = self.app.get(url, user=self.user) 
        staff_response = self.app.get(url, user=self.staff)

        assert 'Product Admin' not in anon_response
        assert 'Product Admin' not in user_response
        assert 'Product Admin' in staff_response

    def test_about(self):
        url = reverse('main_about')
        response = self.app.get(url, user=self.user)

    def test_contact(self):
        url = reverse('main_contact')
        response = self.app.get(url, user=self.user)
    

