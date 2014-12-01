# -*- coding: utf-8 -*-
import pytest
from sale.services.order import get_list_of_orders, import_list_of_orders
from sale.models import Address, Order

import logging
logging.basicConfig(filename="boto.log", level=logging.DEBUG)


@pytest.mark.django_db
def test_import_list_of_orders():

    list_of_orders = get_list_of_orders('amazon_de',
                                        '2014-10-01T00:00:00Z',
                                        '2014-10-05T00:00:00Z')

    import_list_of_orders(list_of_orders)

    assert Order.objects.all().count() == 3
    assert Address.objects.all().count() == 3

    order = Order.objects.get(marketplace_order_id='305-9404636-8008365')
    assert order.marketplace_id == 2
    assert order.price == 1400
    assert order.address.name == 'Patricia Kürthy'
    assert order.address.postal_code == '90574'
