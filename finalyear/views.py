from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Sum

from .models import Transaction, MonthlyPayment, AnnualPayment, Fertilizer

from datetime import datetime

def home(request):
    return render(request, 'generic/indexed.html')

"""
def about(request):
    return render(request, 'finalyear/about.html')
"""

@login_required
def transactions(request):
    print(request.GET.get('search'))
    monthly = Transaction.objects.filter(farmer__username=request.user).filter(date_posted__month = request.GET.get('search'))
    print(monthly)
    transactions = Transaction.objects.filter(farmer__username = request.user)

    context = {
        'transactions' : transactions,
        'monthly' : monthly
        #'fertilizer' : fertilizer,
    }
    return render(request, 'finalyear/transactions.html', context)

@login_required
def monthly_payment_made(request):
    transactions_estimates = Transaction.objects.filter(date_posted__month = datetime.now().month).filter(
        farmer__username = request.user).aggregate(total_kilos = Sum('kilos'))
    if transactions_estimates['total_kilos'] is None:
        estimated_pay = 0
    else:
        estimated_pay = transactions_estimates['total_kilos'] * 14.00

    payments = MonthlyPayment.objects.filter(username=request.user).filter(payment_date__month = datetime.now().month )
    context = {
        'estimated_pay' : estimated_pay,
        'payments' : payments,
        'datetime' : datetime.now(),
    }

    return render(request, 'finalyear/summary.html', context)

@login_required
def annual_payment_made(request):

    fertilizer_cost = Fertilizer.objects.filter(farmer__username=request.user).filter(date_issued__year=datetime.now().year).aggregate(total=Sum('total_cost'))
    transactions_estimates = Transaction.objects.filter(date_posted__month = datetime.now().month).filter(
        farmer__username = request.user).aggregate(total_kilos = Sum('kilos'))
    if transactions_estimates['total_kilos'] is None:
        estimated_pay = 0
    else:
        estimated_pay = transactions_estimates['total_kilos'] * 52.00 - float(fertilizer_cost['total'])

    payments = AnnualPayment.objects.filter(username=request.user).filter(payment_date__year = datetime.now().year )
    context = {
        'estimated_pay' : estimated_pay,
        'payments' : payments,
        'datetime' : datetime.now(),
    }
    return render(request, 'finalyear/summary.html', context)


"""
The code below is recommended to be run in a seperate file
"""

def testing_celery():
    print("This will be running once in the beginning of the month")

def schedule_monthly_payment():
    payments = Transaction.objects.filter(date_posted__month = datetime.now().month - 1).values(
        'farmer__username').annotate(Sum('kilos'))

    for payment in payments:
        #fertilizer = Fertilizer.objects.filter(farmer__username = payment['farmer__username']).
        MonthlyPayment.objects.create(username = payment['farmer__username'],
            amount=payment['kilos__sum']*50,kilos=payment['kilos__sum'])



def schedule_annual_payment():
    payments = Transaction.objects.filter(
        date_posted__year = datetime.now().year).values('farmer__username').annotate(Sum('kilos'))

    for payment in payments:
        total_kilos = list(Fertilizer.objects.filter(farmer__username=payment['farmer__username']).filter(date_issued__year = datetime.now().year).aggregate(Sum('total_cost')).values())[0]
        AnnualPayment.objects.create(username = payment['farmer__username'],
            amount=payment['kilos__sum']*50,kilos=payment['kilos__sum'], deductions=total_kilos)
