from django.shortcuts import render
from django.views import generic

from datetime import date
from utils import get_object_from_api


class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get(self, request):
        aurora_daily_forecast = get_object_from_api("aurora_daily_forecast/?date=" + str(date.today()))

        return render(request, self.template_name, {"aurora_daily_forecast": aurora_daily_forecast})


class AlarmsView(generic.TemplateView):
    template_name = 'alarms.html'


class GalleryView(generic.TemplateView):
    template_name = 'gallery.html'


class MapView(generic.TemplateView):
    template_name = 'map.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'

