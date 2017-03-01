from asyncio.test_utils import mock_nonblocking_socket
from django.db import models

# Create your models here.


class Slide(models.Model):
    """
        Carousel in home page
    """
    img = models.ImageField(upload_to='statics/carousel', height_field=100, width_field=100, max_length=1000)
    short_descr = models.CharField(max_length=30)
    long_descr = models.CharField(max_length=120)


class HomePage(models.Model):
    """
        Images and description of home page
    """
    # Fields
    biography = models.TextField()
    carousel = models.ForeignKey(Slide, on_delete=models.CASCADE)


class News(models.Model):
    """
        News for site
    """
    img = models.ImageField(upload_to='statics/news', height_field=100, width_field=100, max_length=1000)
    title = models.CharField(max_length=50)
    date = models.DateField()
    detail = models.TextField()


class Composition(models.Model):
    """
        Composition of DNL
    """
    img = models.ImageField(upload_to='statics/comps', height_field=100, width_field=100, max_length=1000)
    name = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField(default=0)
    date = models.DateField()
    short_descr = models.CharField(max_length=50)
    detail = models.CharField(max_length=120)
    file = models.FileField(upload_to='statics/comps', max_length=10000)


class Contact(models.Model):
    """
        Information to contact
    """
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
