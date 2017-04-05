from django.conf.urls import url
from . import views

handler404 = views.e404;

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^news/$', views.NewsView.as_view(), name='news'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^comps/$', views.CompositionsView.as_view(), name='comps'),
    url(r'^comps/pay/(?P<pk>\d+)', views.CompositionsView.as_view()),
    url(r'^comp/(?P<pk>\d+)$', views.CompositionDetail.as_view(), name='detail'),
    url(r'^comp/(?P<pk>\d+)/pay$', views.CompositionDetail.as_view()),
    url(r'^search/$', views.search, name='search'),
]
