from django.conf.urls import patterns, url
from tasks import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^project/(?P<project>\d+)/$', views.project, name='project'),
)
