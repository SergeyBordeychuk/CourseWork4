import os
from celery import Celery
from django.conf import settings

app = Celery('CourseWork4', broker='your_broker_url_here')

