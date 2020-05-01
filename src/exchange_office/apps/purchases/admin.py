from django.contrib import admin

from .models import Customer, Purchase


admin.site.register(Customer)
admin.site.register(Purchase)
