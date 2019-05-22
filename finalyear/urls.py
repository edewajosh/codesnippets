from django.urls import path
from finalyear import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('about/', views.about, name='about'),
    path('month/', views.monthly_payment, name = 'monthly_payment'),
    path('annual/', views.annual_payment, name = 'annual_payment'),
    path('msummary/', views.monthly_payment_made, name = 'monthly_payment_made'),
    path('asummary/', views.annual_payment_made, name = 'annual_payment_made'),
    path('transactions/', views.transactions, name='transactions'),
]
