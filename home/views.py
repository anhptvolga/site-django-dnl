from django.shortcuts import render, get_object_or_404
from .models import DnlSiteInfo, Slide, News, Composition
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import FormMixin, FormView, SingleObjectMixin
from .forms import FeedbackForm, BuyForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from dnl.settings import EMAIL_HOST_USER
from django.core.mail import send_mail, EmailMessage


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
    slug_field = ''

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contact_active'] = True
        context['form'] = self.get_form()
        return context

    def get_object(self, queryset=None):
        return DnlSiteInfo.objects.first()

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # form = FeedbackForm(data=request.POST)
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('contact')

    def form_valid(self, form):
        # save message
        mess = form.save()
        messages.success(self.request, 'Thank you for giving feedback! We got it!')
        return super(ContactView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Make sure you entered correctly!')
        return super(ContactView, self).form_valid(form)


class CompositionPay(FormMixin):
    form_class = BuyForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # TODO: seding mail here
        email_address = form.cleaned_data['email']
        email_message = EmailMessage('Sheet from DNL site', 'Thank you!', EMAIL_HOST_USER, [email_address])
        email_message.attach_file(self.object.file.path)
        email_message.send()

        messages.success(self.request, 'Thank you for paying! We send sheet for you!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Make sure you entered correctly!')
        return super().form_invalid(form)


class CompositionDetail(CompositionPay, DetailView):
    """
        View of contact page
    """
    template_name = 'detail.html'
    context_object_name = 'comp'
    model = Composition

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        object = self.get_object()
        context = super(CompositionDetail, self).get_context_data(**kwargs)
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


def e404(request):
    return render(request, '404.html')