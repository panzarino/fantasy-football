from django.conf.urls import patterns, include, url
from django.contrib import admin
from football import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^search/$', views.search),
    url(r'^search/results/$', views.results),
    url(r'^scoreboard/$', views.scoreboard),
    
    # url(r'^admin/', include(admin.site.urls)),
)
