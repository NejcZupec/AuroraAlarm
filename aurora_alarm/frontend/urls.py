from django.conf.urls import patterns, url, include
from django.views.generic import CreateView
from models import PhotoWithLocation
from views import PhotoWithLocationListView

import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^auroral_activity', views.AuroralActivityView.as_view(), name='auroral_activity'),
    url(r'^alarms/$', views.AlarmsView.as_view(), name='alarms'),
    url(r'^map/$', views.MapView.as_view(), name='map'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^logout/$', views.logout_view, name='logout'),

    # gallery
    url(r'^', include('photologue.urls')),
    url(r'^photo-with-location/add$', CreateView.as_view(model=PhotoWithLocation, success_url="/photo-with-location/page/1"), name="gallery-add-photo"),
    url(r'^photo-with-location/page/(?P<page>[0-9]+)/$', PhotoWithLocationListView.as_view(), name='photo-with-location-list'),
)
