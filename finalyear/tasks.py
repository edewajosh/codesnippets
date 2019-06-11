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

# This is task is intended to run on the 1ST daya of every month
@periodic_task(
    run_every = (crontab(0, 0, day_of_month='1')),
    name =  "monthly_payment_made",
    ignore_result = True
)
def calculate_monthly_devidends():
    #monthly_payment_made()
    testing_celery()

# the task below runs on 31 of the last month
@periodic_task(
	run_every = (crontab(0,0, day_of_month='31', month_of_year='12')),
	name = "schedule_annual_payment",
	ignore_result=True
	)
def calculate_annual_payment():
	schedule_annual_payment()

# the task below runs after every 1 minute
@periodic_task(
    run_every = (crontab()),
    name = "some_test_function",
    ignore_result=True
)
def run_this_joke():
    print("Hello Juja, Thank you for making us what we've become")
