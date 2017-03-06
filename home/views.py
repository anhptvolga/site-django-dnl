from django.shortcuts import render
from .models import Contact, HomePage, Slide, News, Composition
# Create your views here.


def home(request):
    """
        View of  page
    """
    bio = HomePage.objects.first()
    car = Slide.objects.filter(home_page=bio)
    return render(request, "home.html", {
        'home_active': True,
        'carousel': car,
        'biodnl': bio,
    })


def news(request):
    """
        View of news page
    """
    news = News.objects.all()
    return render(request, "news.html", {
        'news_active': True,
        'news': news,
    })


def compositions(request):
    """
        View of compositions page
    """
    comps = Composition.objects.all()[:3]
    return render(request, "comps.html", {
        'comps_active': True,
        'comps': comps,
    })


def contact(request):
    """
        View of contact page
    """
    contact = Contact.objects.all()[1]
    return render(request, "contact.html", {
        'contact_active': True,
        'address': contact.address,
        'email': contact.email,
        'phone': contact.phone
    })

