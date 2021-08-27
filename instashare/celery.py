from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instashare.settings')
app = Celery('instashare')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
app.conf.timezone = 'Asia/Kolkata'
app.conf.beat_schedule = {
    'send-lecture-notif': {
        'task': 'home.tasks.task_send_lecture_email',
        'schedule': 15,
    }
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))