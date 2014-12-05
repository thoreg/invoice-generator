# -*- coding: utf-8 -*-
from rest_framework import permissions, viewsets

from m13.sale.models import Order
from m13.sale.serializers.order import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    model = Order
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
