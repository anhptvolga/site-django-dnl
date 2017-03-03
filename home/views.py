from django.shortcuts import render
from .models import Contact
# Create your views here.


def home(request):
    """
        View of  page
    """
    return render(request, "home.html", {
        'home_active': True,
    })


def news(request):
    """
        View of news page
    """
    return render(request, "news.html", {
        'news_active': True,
    })


def compositions(request):
    """
        View of compositions page
    """
    return render(request, "comps.html", {
        'comps_active': True,
    })


def contact(request):
    """
        View of contact page
    """
    contact = Contact.objects.get(pk=1)
    return render(request, "contact.html", {
        'contact_active': True,
        'address': contact.address,
        'email': contact.email,
        'phone': contact.phone
    })

