from models import AuroraDailyForecast

from rest_framework import viewsets

from serializers import AuroraDailyForecastSerializer


class AuroraDailyForecastSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AuroraDailyForecast to be viewed or edited.
    """
    queryset = AuroraDailyForecast.objects.all()
    serializer_class = AuroraDailyForecastSerializer

