from django.contrib import admin

from .models import Coefficient, CommerceValue


class CoefficientAdmin(admin.ModelAdmin):
    list_display = ('id', 'commerce_value', 'amount', 'percent', 'created_at')
    list_display_links = ('id', 'amount', 'percent',)
    search_fields = ('commerce_value', 'amount', 'percent',)
    list_filter = ('commerce_value',)
    fields = ('amount', 'percent',)
    readonly_fields = ( 'commerce_value', 'created_at', 'updated_at')
    save_on_top = True


class CommerceValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    fields = ('name',)
    save_on_top = True


admin.site.register(Coefficient, CoefficientAdmin)
admin.site.register(CommerceValue, CommerceValueAdmin)