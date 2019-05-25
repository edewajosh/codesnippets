from __future__ import absolute_import, unicode_literals
from celery import task
from celery.task.schedules import crontab
from celery.decorators import periodic_task

from finalyear.views import monthly_payment_made, testing_celery, schedule_annual_payment
from finalyear.models import Transaction

"""
@task()
def add_two_numbers():
    print("Hello Celery!")
"""

@periodic_task(
    run_every = (crontab(0, 0, day_of_month='24')),
    name =  "monthly_payment_made",
    ignore_result = True
)
def calculate_monthly_devidends():
    #monthly_payment_made()
    testing_celery()

@periodic_task(
	run_every = (crontab(0,0, day_of_month='31')),
	name = "schedule_annual_payment",
	ignore_result=True
	)
def calculate_annual_payment():
	schedule_annual_payment()