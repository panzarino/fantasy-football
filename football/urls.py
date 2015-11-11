from django.conf.urls import patterns, include, url
from django.contrib import admin
from football import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^search/$', views.search),
    url(r'^search/results/$', views.results),
    url(r'^scoreboard/$', views.scoreboard),
    url(r'^scoreboard/(\d{1,2})/$', views.previous_scoreboard),
    url(r'^team/(\d{1})/$', views.teamnum),
    url(r'^team/$', views.team),
    url(r'^team/new/$', views.new_team),
    url(r'^team/all/$', views.team_list),
    url(r'^points/$', views.player_points),
    url(r'^prediction/$', views.prediction),
    url(r'^team/edit/(\d{1})/$', views.edit_team),
    url(r'^team/edit/$', views.edit),
    
    # url(r'^admin/', include(admin.site.urls)),
)
