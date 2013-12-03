from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
    """
    This model is used for saving user's specific settings (threshold, location,...).
    """

    user = models.OneToOneField(User)
    threshold = models.PositiveSmallIntegerField(default=4)
    receive_daily_alarms = models.BooleanField(default=False)
    receive_real_time_alarms = models.BooleanField(default=False)


class Location(models.Model):
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    latitude = models.DecimalField(max_digits=7, decimal_places=4)


class Aurora(models.Model):
    aurora_date = models.DateField()


class Alarm(models.Model):
    alarm_time = models.DateTimeField()
    alarm_aurora = models.ForeignKey('Aurora')
    #receivers = models.ManyToManyField('User')


class WebBasedAlarm(Alarm):
    kp_number = models.PositiveSmallIntegerField()


class AuroraDailyForecast(models.Model):
    """
    In this table are saved all aurora daily forecasts from http://www.gi.alaska.edu/AuroraForecast/Europe/.
    This data is collected with the celery task, executed every day.

    created = date/time when daily forecast was added
    modified = date/time when daily forecast was updated (last time)
    first_value = aurora daily forecast value. This value is added just first time when forecast is available. (testing)
    current_value = latest parsed aurora forecast value
    date = aurora forecast is for this day
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    first_value = models.IntegerField()
    current_value = models.IntegerField()
    date = models.DateField()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

# This will create a userprofile each time a user is saved if it is created.
post_save.connect(create_user_profile, sender=User)