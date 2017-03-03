from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^news/$', views.news, name='news'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^comps/', views.compositions, name='comps'),
]
