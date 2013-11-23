from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^alarms/$', views.AlarmsView.as_view(), name='alarms'),
    url(r'^gallery/$', views.GalleryView.as_view(), name='gallery'),
    url(r'^map/$', views.MapView.as_view(), name='map'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^logout/$', views.logout_view, name='logout')
)
