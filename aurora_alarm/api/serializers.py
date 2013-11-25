from rest_framework import serializers
from models import AuroraDailyForecast

class AuroraDailyForecastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuroraDailyForecast
        fields = ["date", "first_value", "current_value", "created", "modified", "url", "id"]
