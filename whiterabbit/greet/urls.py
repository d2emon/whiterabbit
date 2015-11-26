from django.conf.urls import patterns, url
from greet import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^service/$', views.service, name='service'),
    url(r'^full/$', views.full, name='full'),
    url(r'^buttons/$', views.buttons, name='buttons'),
)
