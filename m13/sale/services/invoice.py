# -*- coding: utf-8 -*-
#
import logging

from boto.mws.connection import MWSConnection

from sale.models import Invoice, Marketplace, Order

MERCHANT_ID = "A27MO42EOV27PG"

mws = MWSConnection(Merchant=MERCHANT_ID)
mws.host = 'mws.amazonservices.de'


log = logging.getLogger(__name__)


def create_all_invoice_ids(marketplace_name):
    marketplace = Marketplace.objects.filter(name=marketplace_name)
    orders = Order.objects.filter(marketplace=marketplace)
    print("We got {} orders".format(len(orders)))
    for order in orders:
        invoice, created = Invoice.objects.get_or_create(order=order)

        if created:
            print('Invoice {} created for order {}'.format(invoice.invoice_number,
                                                           order.marketplace_order_id))
        else:
            print('Invoice {} for order {} already in the database'.format(
                invoice.invoice_number, order.marketplace_order_id))


def create_invoice_for_order(order):
    invoice, created = Invoice.objects.get_or_create(order=order)
    if created:
        print('Invoice {} created for order {}'.format(invoice.invoice_number,
                                                       order.marketplace_order_id))
    else:
        print('Invoice {} for order {} already in the database'.format(
              invoice.invoice_number, order.marketplace_order_id))
