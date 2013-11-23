from django.views import generic


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class AlarmsView(generic.TemplateView):
    template_name = 'alarms.html'


class GalleryView(generic.TemplateView):
    template_name = 'gallery.html'


class MapView(generic.TemplateView):
    template_name = 'map.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'
