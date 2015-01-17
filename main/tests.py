from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase

from django_webtest import WebTest

from .models import User, RecipeIdea
from .factories import NormalUserFactory, StaffUserFactory, RecipeIdeaFactory
from products.factories import ProductFactory


class AccessMixin(object):
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

        
class MainSetUp(TestCase):
    def setUp(self):
        self.user = NormalUserFactory.create()
        self.staff = StaffUserFactory.create()
        self.recipe_idea = RecipeIdeaFactory.create()
        self.product = ProductFactory.create(title="Main Test Product")


class MainModelTest(MainSetUp):
    def test_recipe(self):
        recipe = RecipeIdea.objects.get(name=self.recipe_idea.name)


class MainViewTest(MainSetUp, WebTest):
    def setUp(self):
        MainModelTest.setUp(self)

    def test_home(self):
        url = reverse('main_home')
        response = self.app.get(url)

        assert self.product.title in response

    def test_product_admin(self):
        url = reverse('main_home')
        anon_response = self.app.get(url)
        user_response = self.app.get(url, user=self.user) 
        staff_response = self.app.get(url, user=self.staff)

        admin_text = 'glyphicon-cog'

        assert admin_text not in anon_response
        assert admin_text not in user_response
        assert admin_text in staff_response

    def test_about(self):
        url = reverse('main_about')
        response = self.app.get(url)

    def test_contact(self):
        url = reverse('main_contact')
        response = self.app.get(url)

    def test_recipe_ideas(self):
        url = reverse('main_recipe_ideas')
        response = self.app.get(url)

        assert self.recipe_idea.name in response

    def test_robots(self):
        url = reverse('main_robots')
        response = self.app.get(url)
    

