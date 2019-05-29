from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Sum

from .models import Transaction, MonthlyPayment, AnnualPayment

from datetime import datetime

def home(request):
    return render(request, 'finalyear/index.html')

def about(request):
    return render(request, 'finalyear/about.html')

@login_required
def transactions(request):

    transactions = Transaction.objects.filter(farmer__username = request.user)
    context = {
        'transactions' : transactions,
    }
    return render(request, 'finalyear/transactions.html', context)

def monthly_payment(request):
    total_kilos = list(Transaction.objects.filter(farmer__username=request.user).filter(date_posted__month = datetime.now().month).aggregate(Sum('kilos')).values())[0]
    amount = total_kilos * 15
    transactions = MonthlyPayment.objects.get_or_create(farmer=request.user,
                                                    payment_date__month = datetime.now().month,
                                                    amount = amount,
                                                    kilos =  total_kilos,)
    return redirect('home')

@login_required
def monthly_payment_made(request):

    payments = MonthlyPayment.objects.filter(farmer__username=request.user).filter(payment_date__month = datetime.now().month )
    context = {
        'payments' : payments,
        'datetime' : datetime.now(),
    }

    #print("I will be running after every 1 minute")
    return render(request, 'finalyear/summary.html', context)

def annual_payment(request):
    total_kilos = list(Transaction.objects.filter(farmer__username=request.user).filter(date_posted__year = datetime.now().year).aggregate(Sum('kilos')).values())[0]
    amount = total_kilos * 45
    transactions = AnnualPayment.objects.get_or_create(farmer=request.user,
                                                    payment_date__year = datetime.now().year,
                                                    amount = amount,
                                                    kilos =  total_kilos,)
    return redirect('home')

@login_required
def annual_payment_made(request):
    payments = AnnualPayment.objects.filter(farmer__username=request.user).filter(payment_date__year = datetime.now().year )
    context = {
        'payments' : payments,
        'datetime' : datetime.now(),
    }
    return render(request, 'finalyear/summary.html', context)


"""
The code below is moved to a different file
"""

def testing_celery():
    print("This will be running once in the beginning of the month")

def schedule_monthly_payment():
    payments = Transaction.objects.filter(date_posted__month = datetime.now().month - 1).values(
        'farmer__username').annotate(Sum('kilos'))

def schedule_annual_payment():
    payments = Transaction.objects.filter(
        date_posted__year = datetime.now().year).values('farmer__username').annotate(Sum('kilos'))

    # the farmer raises raises an error that it the value must be an User instance
    # since it is a foreing key that inherits from User model
    # to be FIXED
    for payment in payments:
        AnnualPayment.objects.create(username = payment['farmer__username'],
            amount=payment['kilos_sum']*50,kilos=payment['kilos_sum'])
