from django.shortcuts import render, get_object_or_404
from .models import DnlSiteInfo, Slide, News, Composition
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import FormMixin, FormView
from .forms import FeedbackForm

def home(request):
    """
        View of page
    """
    bio = DnlSiteInfo.objects.first()
    car = Slide.objects.filter(home_page=bio)
    return render(request, "home.html", {
        'home_active': True,
        'carousel': car,
        'biodnl': bio,
    })


class NewsView(ListView):
    """
        View of news page
    """
    template_name = "news.html"
    queryset = News.objects.order_by('-date')
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context['news_active'] = True
        return context


class CompositionsView(ListView):
    """
        View of compositions page
    """
    template_name = 'comps.html'
    queryset = Composition.objects.all()[:3]
    context_object_name = 'comps'

    def get_context_data(self, **kwargs):
        context = super(CompositionsView, self).get_context_data(**kwargs)
        context['comps_active'] = True
        return context


class ContactView(FormMixin, DetailView):
    """
        View of contact page
    """
    template_name = 'contact.html'
    form_class = FeedbackForm
    context_object_name = 'contact'
    success_url = '/contact/'
    slug_field = ''

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contact_active'] = True
        return context

    def get_object(self, queryset=None):
        return DnlSiteInfo.objects.first()


class CompDetailView(DetailView):
    """
        View of contact page
    """
    template_name = 'detail.html'
    context_object_name = 'comp'
    model = Composition

    def get_context_data(self, **kwargs):
        context = super(CompDetailView, self).get_context_data(**kwargs)
        context['comps_active'] = True
        return context


def search(request):
    """
        Search page
    """
    searching = request.GET['search'] if 'search' in request.GET else ''
    results = Composition.objects.filter(name__contains=request.GET['search'])
    return render(request, "search.html", {
        'results': results,
        'searching': searching,
    })
