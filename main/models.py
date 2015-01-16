from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.text import slugify


class TimeStampedModel(models.Model):
    '''
    An abstract base class model that provides selfupdating
    created and modified fields.
    '''
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class SaveSlug(models.Model):
    '''
    Base class to create a slugfield
    '''

    slug = models.SlugField(db_index=True, unique=True, 
        editable=False, blank=True)
    title = models.CharField(max_length=40)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        '''
        set the slug based on the title field
        '''
        self.slug = slugify(self.title)
        super(SaveSlug, self).save(*args, **kwargs)  

    def __str__(self):
        return self.title 


class User(AbstractUser):
    '''
    Extended User class. Set this up in the beginning unless you are
    absolutely sure the User class will not expand.
    '''
    
    class Meta:
        db_table = 'auth_user'


class RecipeIdea(models.Model):
    '''
    Simple model to give the readers some recipe and preparation ideas
    '''
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name 
    