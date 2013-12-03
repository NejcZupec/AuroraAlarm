from django.contrib.auth.models import User
from django.http import HttpResponse
from models import AuroraDailyForecast
from rest_framework import viewsets, permissions
from serializers import AuroraDailyForecastSerializer, UserSerializer

import json, datetime


class AuroraDailyForecastSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AuroraDailyForecast to be viewed or edited.
    """
    queryset = AuroraDailyForecast.objects.all()
    serializer_class = AuroraDailyForecastSerializer
    filter_fields = ["first_value", "current_value", "date"]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser, )


def aurora_activity_chart_data_json(request):
    """
    Ugly hack! Preparing JSON object appropriate for highchart's chart.
    TODO: this solution should be improved. We have to find out, have to create RESTful request to API, to get
    appropriate JSON object.
    """

    values = AuroraDailyForecast.objects.all()
    data = [[convert_python_date_to_highchart_format(value.date), value.current_value] for value in values]

    return HttpResponse(json.dumps(data), mimetype="application/json")


def convert_python_date_to_highchart_format(python_date):
    """
    TODO: This function should be removed. Read comment at aurora_activity_chart_data_json comment.
    """
    year, month, day = str(python_date).split('-')
    d = datetime.datetime(int(year), int(month), int(day), 0, 0, 0, 0)

    return int(d.strftime('%s')+"000")
