from celery.task.schedules import crontab
from celery import task
from celery.decorators import periodic_task, task
from orders.cart import Cart
from celery.utils.log import get_task_logger


    