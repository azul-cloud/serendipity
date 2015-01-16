from factory.django import DjangoModelFactory

from django.contrib.auth import get_user_model

from .models import RecipeIdea

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User


class NormalUserFactory(UserFactory):
    username = 'normaluser'
    password = 'normalpassword'
    email = 'user@email.com'
    first_name = 'John'
    last_name = 'Doe'


class AdminUserFactory(UserFactory):
    username = 'adminuser'
    password = 'adminpassword'
    email = 'admin@email.com'
    first_name = 'Admin'
    last_name = 'User'
    is_staff = True
    is_admin = True


class StaffUserFactory(UserFactory):
    username = 'staffuser'
    password = 'staffpassword'
    email = 'staff@email.com'
    first_name = 'Staff'
    last_name = 'User'
    is_staff = True


class RecipeIdeaFactory(DjangoModelFactory):
    class Meta:
        model = RecipeIdea


