from django.contrib import admin

from m13.sale.models import Address, Marketplace, Order, Invoice


class ReadOnlyTabularInline(admin.TabularInline):
    extra = 0
    can_delete = False
    editable_fields = []
    readonly_fields = []
    exclude = []

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
            [field.name for field in self.model._meta.fields
                if field.name not in self.editable_fields and field.name not in self.exclude]

    def has_add_permission(self, request):
        return False


class MarketplaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor_id')


class OrderInline(ReadOnlyTabularInline):
    model = Order


class InvoiceInline(ReadOnlyTabularInline):
    model = Invoice


class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'street', 'postal_code', 'country_code')
    inlines = [
        OrderInline,
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ('marketplace_order_id',)
    inlines = [
        InvoiceInline,
    ]


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number',)


admin.site.register(Marketplace, MarketplaceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Invoice, InvoiceAdmin)
