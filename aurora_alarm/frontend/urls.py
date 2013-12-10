from django.conf.urls import patterns, url, include
import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^auroral_activity', views.AuroralActivityView.as_view(), name='auroral_activity'),
    url(r'^alarms/$', views.AlarmsView.as_view(), name='alarms'),
    url(r'^', include('photologue.urls')),
    url(r'^map/$', views.MapView.as_view(), name='map'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^logout/$', views.logout_view, name='logout')
)
