from django.shortcuts import render_to_response
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'index.html'