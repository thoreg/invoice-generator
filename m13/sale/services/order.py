# -*- coding: utf-8 -*-
#
import logging

from boto.mws.connection import MWSConnection

from m13.sale.models import Address, Marketplace, Order

MERCHANT_ID = "A27MO42EOV27PG"

mws = MWSConnection(Merchant=MERCHANT_ID)
mws.host = 'mws.amazonservices.de'


log = logging.getLogger(__name__)


def get_list_of_orders(marketplace_name, start_datetime, end_datetime):

    marketplace_id_list = Marketplace.objects.filter(name=marketplace_name) \
                                             .values_list('vendor_id', flat=True)
    print("   marketplace_id_list: {}".format(marketplace_id_list))
    print("   start: {}".format(start_datetime))
    print("   end: {}".format(end_datetime))
    response = mws.list_orders(CreatedAfter=start_datetime,
                               CreatedBefore=end_datetime,
                               MarketplaceId=marketplace_id_list)

    '''
    from pprint import pprint
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

        print("\nEntry: ")
        print(entry.__dict__)

        if entry.OrderStatus == 'Canceled':
            print('order: {} canceled - skipping'.format(entry.AmazonOrderId))
            continue

        if entry.ShippingAddress is None:
            print('order: {} no shipping address - skipping'.format(entry.AmazonOrderId))
            continue

        print("Address: ")
        print(entry.ShippingAddress.__dict__)

        address_lines = []
        if hasattr(entry.ShippingAddress, 'AddressLine1'):
            address_lines.append(entry.ShippingAddress.AddressLine1)
        if hasattr(entry.ShippingAddress, 'AddressLine2'):
            address_lines.append(entry.ShippingAddress.AddressLine2)
        if hasattr(entry.ShippingAddress, 'AddressLine3'):
            address_lines.append(entry.ShippingAddress.AddressLine3)
        street = "\n".join(address_lines)
        log.debug("Street: {}".format(street))

        address, _created = Address.objects.get_or_create(name=entry.ShippingAddress.Name,
                                                          city=entry.ShippingAddress.City,
                                                          street=street,
                                                          postal_code=entry.ShippingAddress.PostalCode,
                                                          country_code=entry.ShippingAddress.CountryCode)

        price_in_cent = int(entry.OrderTotal.Amount * 100)
        marketplace = Marketplace.objects.get(name='amazon_de')

        order, created = Order.objects.get_or_create(marketplace_order_id=entry.AmazonOrderId,
                                                     defaults={'purchase_time': entry.PurchaseDate,
                                                               'price': price_in_cent,
                                                               'email': entry.BuyerEmail,
                                                               'marketplace': marketplace,
                                                               'address': address})
        if created:
            log.info('order: {} created'.format(order.marketplace_order_id))
        else:
            log.info('order: {} already in the database'.format(order.marketplace_order_id))


def import_all_orders(marketplace_name):
    DATES = [("2014-09-01T00:00:00Z", "2014-10-01T00:00:00Z"),
             ("2014-10-01T00:00:00Z", "2014-11-01T00:00:00Z"),
             ("2014-11-01T00:00:00Z", "2014-12-01T00:00:00Z"),
             ("2014-12-01T00:00:00Z", "2014-12-03T00:00:00Z")]

    for start, end in DATES:
        print("{} {} {}".format(marketplace_name, start, end))
        orders = get_list_of_orders(marketplace_name, start, end)
        import_list_of_orders(orders)
