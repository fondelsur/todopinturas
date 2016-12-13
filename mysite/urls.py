from django.conf.urls import include, url
from django.contrib import admin
from polls import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^datos/', include('polls.urls')),
    url(r'^$', views.IndexWithSearch.as_view(), name='index')
]
