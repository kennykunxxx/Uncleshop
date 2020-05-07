from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fishshop.settings')
app = Celery('fishshop')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

"""
app.conf.beat_schedule = {
    'every three hours check': {
        'task': 'cart_check',
        'schedule': crontab(minute='*/1'),
    }
}
"""