from django.contrib import admin

from sale.models import Address, Marketplace, Order


class MarketplaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor_id')


class AddressInline(admin.TabularInline):
    model = Address


class OrderAdmin(admin.ModelAdmin):
    list_display = ('marketplace_order_id',)
    inlines = [
        AddressInline,
    ]

admin.site.register(Marketplace, MarketplaceAdmin)
admin.site.register(Order, OrderAdmin)
