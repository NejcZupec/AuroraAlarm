from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

import views


# Router for API navigation.
router = DefaultRouter()
router.register(r'aurora_daily_forecast', views.AuroraDailyForecastSet)
router.register(r'users', views.UserViewSet)
router.register(r'user_profiles', views.UserProfileViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^aurora_activity_chart_data_json/$', views.aurora_activity_chart_data_json),
)
