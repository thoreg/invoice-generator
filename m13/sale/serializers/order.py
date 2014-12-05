# -*- coding: utf-8 -*-

from rest_framework import serializers

from m13.sale.models import Order


class OrderSerializer(serializers.ModelSerializer):
    marketplace_name = serializers.CharField(source='marketplace.name')
    customer_name = serializers.CharField(source='address.name')
    invoice_number = serializers.CharField(source='get_invoice_number')

    class Meta:
        model = Order
        fields = ('marketplace_order_id', 'purchase_time', 'marketplace_name',
                  'customer_name', 'invoice_number')
