from django.contrib.auth.models import User
from rest_framework import serializers
from models import AuroraDailyForecast

class AuroraDailyForecastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuroraDailyForecast
        fields = ["date", "first_value", "current_value", "created", "modified", "url", "id"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "username", "email", "groups")
