from django.contrib import admin
from sale.models import Marketplace


class MarketplaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor_id')

admin.site.register(Marketplace, MarketplaceAdmin)
