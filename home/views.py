from django.shortcuts import render, get_object_or_404
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
    ns = News.objects.all()
    return render(request, "news.html", {
        'news_active': True,
        'news': ns,
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
    ct = Contact.objects.all()[1]
    return render(request, "contact.html", {
        'contact_active': True,
        'address': ct.address,
        'email': ct.email,
        'phone': ct.phone
    })


def detail(request, cmp_pk):
    """
        View of contact page
    """
    print(cmp_pk)
    cmp = get_object_or_404(Composition, pk=cmp_pk)
    return render(request, "detail.html", {
        'comps_active': True,
        'comp': cmp,
    })
