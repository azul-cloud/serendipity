from django.db import models
from django.contrib.auth.models import AbstractUser


class TimeStampedModel(models.Model):
    '''
    An abstract base class model that provides selfupdating
    created and modified fields.
    '''
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class SaveSlugBase(models.Model):
    '''
    Base class to create a slugfield
    '''

    slug = models.SlugField(db_index=True, unique=True, 
        editable=False, blank=True)

    class Meta:
        abstract = True


class SaveSlugTitle(SaveSlugBase):
    '''
    create a title field with the autosave slug field
    '''
    title = models.CharField(max_length=40)

    def save(self, *args, **kwargs):
        '''
        set the slug based on the title field
        '''
        self.slug = slugify(self.title)
        super(SaveSlugTitle, self).save(*args, **kwargs)   

    class Meta:
        abstract = True


class SaveSlugName(SaveSlugBase):
    '''
    create a name field with the autosave slug field
    '''
    name = models.CharField(max_length=40)

    def save(self, *args, **kwargs):
        '''
        set the slug based on the name field
        '''
        self.slug = slugify(self.name)
        super(SaveSlugName, self).save(*args, **kwargs)   

    class Meta:
        abstract = True


class User(AbstractUser):
    '''
    Extended User class. Set this up in the beginning unless you are
    absolutely sure the User class will not expand.
    '''
    alive = models.BooleanField(default=True)
    