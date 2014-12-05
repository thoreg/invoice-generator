# -*- coding: utf-8 -*-

from rest_framework import serializers

from m13.sale.models import Order


class OrderSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='address.name')
    invoice_number = serializers.CharField(source='get_invoice_number')

    class Meta:
        model = Order
        fields = ('marketplace_order_id', 'purchase_time', 'marketplace',
                  'name', 'invoice_number')
