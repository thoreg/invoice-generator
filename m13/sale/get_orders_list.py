# -*- coding: utf-8 -*-
#
from decimal import Decimal
from pprint import pprint

from boto.mws.connection import MWSConnection

MERCHANT_ID = "A27MO42EOV27PG"
MARKETPLACE_ID_AMAZON_DE = "A1PA6795UKMFR9"

mws = MWSConnection(Merchant=MERCHANT_ID)
mws.host = 'mws.amazonservices.de'

DATES = [("2014-09-01T00:00:00Z", "2014-10-01T00:00:00Z"),
         ("2014-10-01T00:00:00Z", "2014-11-01T00:00:00Z"),
         ("2014-11-01T00:00:00Z", "2014-11-22T00:00:00Z")]

for start, end in DATES:
    response = mws.list_orders(CreatedAfter=start,
                               CreatedBefore=end,
                               MarketplaceId=[MARKETPLACE_ID_AMAZON_DE, ])

    number_of_orders = len(response.ListOrdersResult.Orders.Order)
    total_order_sum = 0

    for order in response.ListOrdersResult.Orders.Order:
        print
        print order.AmazonOrderId, order.PurchaseDate, order.OrderTotal
        pprint(order)

        if order.OrderTotal is not None:
            total_order_sum += order.OrderTotal.Amount

    print
    print "Zeitraum: {} - {}".format(start, end)
    print "Anzahl der Bestellungen: {0:>11}".format(number_of_orders)
    print "Umsatz (Brutto): {0:>19.2f}".format(total_order_sum)
    print "Umsatz (Netto): {0:>20.2f}".format(total_order_sum / Decimal(1.19))
    print

