"""
Let's say we want to create a list action to apply  a 10% discount to the selected books.
It would be as simple as :
"""
import decimal
from django.contrib import admin
from .models import Book

def apply_dicount(modeladmin, request, queryset):
    for book in queryset:
        book.price = book.price * decimal.Decimal('0.9')
        book.save()
apply_dicount.short_description = 'Apply 10%% discount'

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publication_date', 'author', 'price', 'book_type']
    actions = [apply_dicount, ] # <-- Add the list action function here
    
admin.site.register(Book, BookAdmin)
