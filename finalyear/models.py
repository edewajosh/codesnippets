from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Center(models.Model):
    name = models.CharField(max_length = 150)
    location = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    kilos = models.FloatField()
    date_posted = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.kilos)

class MonthlyPayment(models.Model):
    # At extreme point we could assign a farmer field a value directly
    # of course it will be unique
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    kilos = models.FloatField()
    payment_date = models.DateField(default=datetime.now)
    paid = models.BooleanField(default=True)

    def __str__(self):
        return str(self.amount)

class AnnualPayment(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    kilos = models.FloatField()
    payment_date = models.DateField(default=datetime.now)
    paid = models.BooleanField(default=True)

    def __str__(self):
        return str(self.amount)

