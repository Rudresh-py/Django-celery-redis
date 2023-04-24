from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func
from send_mail_app.tasks import send_email_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json


# Create your views here.

def test(request):
    test_func.delay()
    return HttpResponse("Done")


def send_mail_to_all(request):
    send_email_func.delay()
    return HttpResponse("sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=22, minute=38)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_email_task" + "7", task='send_mail_app.tasks.send_email_func',
                                       )
    return HttpResponse("Done")
