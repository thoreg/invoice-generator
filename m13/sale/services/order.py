# -*- coding: utf-8 -*-
#
import logging
from decimal import Decimal
from pprint import pprint

from boto.mws.connection import MWSConnection

from sale.models import Order, Address, Marketplace

MERCHANT_ID = "A27MO42EOV27PG"

mws = MWSConnection(Merchant=MERCHANT_ID)
mws.host = 'mws.amazonservices.de'

DATES = [("2014-09-01T00:00:00Z", "2014-10-01T00:00:00Z"),
         ("2014-10-01T00:00:00Z", "2014-11-01T00:00:00Z"),
         ("2014-11-01T00:00:00Z", "2014-11-22T00:00:00Z")]

log = logging.getLogger(__name__)


def get_list_of_orders(marketplace_name, start_datetime, end_datetime):

    marketplace_id_list = Marketplace.objects.filter(name=marketplace_name) \
                                             .values_list('vendor_id', flat=True)
    response = mws.list_orders(CreatedAfter=start_datetime,
                               CreatedBefore=end_datetime,
                               MarketplaceId=marketplace_id_list)

    '''
    number_of_orders = len(response.ListOrdersResult.Orders.Order)
    total_order_sum = 0

    for order in response.ListOrdersResult.Orders.Order:
        print
        print order.AmazonOrderId, order.PurchaseDate, order.OrderTotal
        pprint(order)

        if order.OrderTotal is not None:
            total_order_sum += order.OrderTotal.Amount

    print
    print "Zeitraum: {} - {}".format(start_datetime, end_datetime)
    print "Anzahl der Bestellungen: {0:>11}".format(number_of_orders)
    print "Umsatz (Brutto): {0:>19.2f}".format(total_order_sum)
    print "Umsatz (Netto): {0:>20.2f}".format(total_order_sum / Decimal(1.19))
    print
    '''

    return response.ListOrdersResult.Orders.Order


def import_list_of_orders(list_of_orders):

    for entry in list_of_orders:
        address_lines = []
        if 'AddressLine1' in entry.ShippingAddress:
            address_lines.append(entry.ShippingAddress.AddressLine1)
        if 'AddressLine2' in entry.ShippingAddress:
            address_lines.append(entry.ShippingAddress.AddressLine2)
        if 'AddressLine3' in entry.ShippingAddress:
            address_lines.append(entry.ShippingAddress.AddressLine3)
        street = "\n".join(address_lines)

        address, _created = Address.objects.get_or_create(name=entry.ShippingAddress.Name,
                                                          city=entry.ShippingAddress.City,
                                                          street=street,
                                                          state=entry.ShippingAddress.StateOrRegion,
                                                          postal_code=entry.ShippingAddress.PostalCode,
                                                          country_code=entry.ShippingAddress.CountryCode)

        price_in_cent = int(entry.OrderTotal.Amount)*100
        marketplace = Marketplace.objects.get(name='amazon_de')

        order, created = Order.objects.get_or_create(marketplace_order_id=entry.AmazonOrderId,
                                                     defaults={'purchase_time': entry.PurchaseDate,
                                                               'price': price_in_cent,
                                                               'email': entry.BuyerEmail,
                                                               'marketplace': marketplace,
                                                               'address': address})
        if created:
            log.info('order: {} created'.format(order))
        else:
            log.info('order: {} already in the database'.format(order))

        for o in Order.objects.all():
            pprint(o.__dict__)
            pprint(o.address.__dict__)

        print("Orders: {}".format(Order.objects.all().count()))
        print("Address: {}".format(Address.objects.all().count()))

