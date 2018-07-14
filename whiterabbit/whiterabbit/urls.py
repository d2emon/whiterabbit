from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^answer/', include('answerer.urls', namespace="answerer")),
    url(r'^greet/', include('greet.urls', namespace="greet")),
    url(r'^', include('greet.urls')),
    url(r'^task/', include('tasks.urls', namespace="tasks")),
]
