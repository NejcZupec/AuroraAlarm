from django.contrib.auth.models import User
from rest_framework import serializers
from models import AuroraDailyForecast, UserProfile


class AuroraDailyForecastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuroraDailyForecast
        fields = ["date", "first_value", "current_value", "created", "modified", "url", "id"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "groups", "userprofile"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["user", "threshold", "receive_daily_alarms", "receive_real_time_alarms"]
