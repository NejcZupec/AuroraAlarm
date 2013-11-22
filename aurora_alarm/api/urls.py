from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

import views


# Router for API navigation.
router = DefaultRouter()
router.register(r'aurora_daily_forecast', views.AuroraDailyForecastSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)





