# from __future__ import absolute_import
# from celery import shared_task
from instashare.celery import app
from datetime import datetime

import pytz
from django.utils import timezone
# from datetime import time, timezone
from home.models import Batch, Lecture
from users.models import Profile
from django.core.mail import send_mail
from django.db.models import Q

@app.task
def send_email_to_batch(batch_id,lecture_id):
    batch = Batch.objects.get(pk=batch_id)
    lecture = Lecture.objects.get(pk=lecture_id)
    for user in Profile.objects.filter(batch=batch):
        print(user)
        send_mail(
            f'{lecture.subject_name}',
           f'Hi {user.user.username} your {lecture.subject_name} is schedule from {lecture.start_time} to {lecture.end_time}.',
            'arihantjainbansa@gmail.com',
            [user.user.email],
            fail_silently=False,
        )

@app.task
def task_send_lecture_email():
    print("HI")
    # send_mail(
    # 'Subject here',
    # 'Here is the message.',
    # 'arihantjainbansa@gmail.com',
    # ['arihantjainbansa@gmail.com'],
    # fail_silently=False,
    #     )
    time_now = timezone.localtime(timezone.now()) 
    time_after_thirty_minute = time_now + timezone.timedelta(minutes=30)
    print(time_now)
    print(time_after_thirty_minute)
    for batch in Batch.objects.all():
        for lecture in Lecture.objects.filter(batch=batch,start_time__gte=time_now,start_time__lte=time_after_thirty_minute):
            send_email_to_batch.delay(batch.id,lecture.id)

