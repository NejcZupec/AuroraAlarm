from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views import generic

from datetime import date
from utils import get_object_from_api


class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request):
        aurora_daily_forecast = get_object_from_api("aurora_daily_forecast/?date=" + str(date.today()))

        return render(request, self.template_name, {"aurora_daily_forecast": aurora_daily_forecast})


class AuroralActivityView(generic.TemplateView):
    template_name = 'auroral_activity.html'


class AlarmsView(generic.TemplateView):
    template_name = 'alarms.html'


class GalleryView(generic.TemplateView):
    template_name = 'gallery.html'


class MapView(generic.TemplateView):
    template_name = 'map.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

