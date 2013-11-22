from rest_framework import serializers
from models import AuroraDailyForecast

class AuroraDailyForecastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuroraDailyForecast