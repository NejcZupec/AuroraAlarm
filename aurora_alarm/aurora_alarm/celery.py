from __future__ import absolute_import
from celery import Celery
from datetime import timedelta
from django.conf import settings

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aurora_alarm.settings')

app = Celery('aurora_alarm')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(
    CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
    CELERY_TIMEZONE='Europe/Stockholm',
)

CELERYBEAT_SCHEDULE = {
    'hello-world-every-10-seconds': {
        'task': 'hello_world',
        'schedule': timedelta(seconds=10)
    }
}


@app.task(bind=True)
def hello_world(self):
    return "Hello world!"

