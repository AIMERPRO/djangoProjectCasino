from django.contrib import admin

from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

from .models import Currency, Country

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    ordering = ('slug',)
    
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
admin.site.register(Country, CountryAdmin)
admin.site.register(Currency, CurrencyAdmin)