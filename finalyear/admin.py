# cashmunene@1234
from django.contrib import admin
from django.contrib.admin import AdminSite

from finalyear.models import Center, Transaction, AnnualPayment, MonthlyPayment, Fertilizer

class FinalyearAdminSite(AdminSite):
    pass

class CenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'location','description')


class MonthlyAdmin(admin.ModelAdmin):
    list_display = ('username', 'kilos','amount', 'payment_date', 'paid')

class AnnualAdmin(admin.ModelAdmin):
    list_display = ('username', 'kilos','amount', 'deductions', 'payment_date', 'net_pay','paid')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('center', 'farmer', 'kilos', 'date_posted')

class FertilizerAdmin(admin.ModelAdmin):
    list_display = ('farmer','date_issued', 'number_of_bags', 'weight', 'total_weight', 'total_cost')

admin.site.siter_header = "Tea Farmers Admin"
admin.site.siter_title = "Tea Farmers Admin Portal"
admin.site.index_index = "Welcome to Tea Farmers Portal"


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Center, CenterAdmin)
#admin.site.register(Farmer, FarmerAdmin)
admin.site.register(AnnualPayment, AnnualAdmin)
admin.site.register(MonthlyPayment,MonthlyAdmin)
admin.site.register(Fertilizer, FertilizerAdmin)
