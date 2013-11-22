from django.db import models

# Create your models here.
class AuroraDailyForecast(models.Model):
    """
    In this table are saved all aurora daily forecasts from http://www.gi.alaska.edu/AuroraForecast/Europe/.
    This data is collected with the celery task, executed every 5 minutes.

    created = date/time when daily forecast was added
    modified = date/time when daily forecast was updated (last time)
    first_value = aurora daily forecast value. This value is added just first time when forecast is available. (testing)
    current_value = latest parsed aurora forecast value
    """

    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)
    first_value = models.IntegerField()
    current_value = models.IntegerField()

