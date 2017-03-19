from asyncio.test_utils import mock_nonblocking_socket
from django.db import models
from django.urls import reverse

# Create your models here.


class DnlSiteInfo(models.Model):
    """
        Images and description of home page
    """
    # Fields
    biography = models.TextField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()


class Slide(models.Model):
    """
        Carousel in home page
    """
    img = models.ImageField(upload_to='media/carousel')
    short_descr = models.CharField(max_length=30)
    long_descr = models.CharField(max_length=120)
    home_page = models.ForeignKey(DnlSiteInfo, on_delete=models.CASCADE, default=None)


class News(models.Model):
    """
        News for site
    """
    img = models.ImageField(upload_to='media/news')
    title = models.CharField(max_length=50)
    date = models.DateField()
    detail = models.TextField()


class Composition(models.Model):
    """
        Composition of DNL
    """
    img = models.ImageField(upload_to='media/comps')
    name = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField(default=0)
    date = models.DateField()
    short_descr = models.CharField(max_length=50)
    detail = models.TextField()
    file = models.FileField(upload_to='media/comps')

    def get_absolute_url(self):
        """
        Returns the url to access a particular composition instance.
        """
        return reverse('detail', args=[str(self.pk)])


class Feedback(models.Model):
    """
        Feedback from user
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
