from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^news/$', views.NewsView.as_view(), name='news'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^comps/$', views.CompositionsView.as_view(), name='comps'),
    url(r'^comp/(?P<pk>\d+)$', views.CompDetailView.as_view(), name='detail'),
    url(r'^search/$', views.search, name='search'),
]
