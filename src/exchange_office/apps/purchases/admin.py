from django.contrib import admin

from .models import Customer, Purchase


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'created_at')
    list_display_links = ('id', 'first_name',)
    search_fields = ('first_name', 'last_name', 'phone_number',)
    list_filter = ('first_name', 'last_name',)
    fields = ('first_name', 'last_name', 'phone_number', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    save_on_top = True


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'currency', 'exchange_currency', 'value', 'created_at')
    list_display_links = ('id', 'value')
    search_fields = ('customer', 'value', 'currency', 'exchange_currency',)
    list_filter = ('customer', 'currency', 'exchange_currency',)
    fields = ('value', 'customer', 'currency', 'exchange_currency', 'created_at', 'updated_at')
    readonly_fields = ('customer', 'currency', 'exchange_currency', 'created_at', 'updated_at')
    save_on_top = True


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Purchase, PurchaseAdmin)

admin.site.site_title = 'Управление заявками'
admin.site.site_header = 'Управление заявками'