from django.urls import path
from finalyear import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('msummary/', views.monthly_payment_made, name = 'monthly_payment_made'),
    path('asummary/', views.annual_payment_made, name = 'annual_payment_made'),
    path('transactions/', views.transactions, name='transactions'),
]
