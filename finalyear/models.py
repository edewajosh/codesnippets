from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Center(models.Model):
    name = models.CharField(max_length = 150)
    location = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name

"""
class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.IntegerField()
    phonenumber = models.IntegerField()

    def __str__(self):
        return self.firstname + " " + self.lastname
"""

class Transaction(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    kilos = models.FloatField()
    date_posted = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.kilos)

class MonthlyPayment(models.Model):
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

