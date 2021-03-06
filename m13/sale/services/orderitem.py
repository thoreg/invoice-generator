# -*- coding: utf-8 -*-
import logging
from datetime import date, datetime, timedelta

from boto.mws.connection import MWSConnection

from m13.sale.models import Order, OrderItem, Product, Marketplace
from m13.sale.services.order import get_list_of_orders, import_list_of_orders
from m13.sale.services.invoice import create_invoice_for_order


MERCHANT_ID = "A27MO42EOV27PG"

mws = MWSConnection(Merchant=MERCHANT_ID)
mws.host = 'mws.amazonservices.de'


log = logging.getLogger(__name__)


def get_orderitems(order_id):
    response = mws.list_order_items(AmazonOrderId=order_id)
    return response.ListOrderItemsResult.OrderItems.OrderItem


def import_orderitems(marketplace_order_id):

    print("\nImport OrderItems for Order: {}".format(marketplace_order_id))
    try:
        order = Order.objects.get(marketplace_order_id=marketplace_order_id)
    except Order.DoesNotExist():
        log.error("Order: {} not found".format(marketplace_order_id))
        return

    list_of_orderitems = get_orderitems(marketplace_order_id)

    print(list_of_orderitems)

    for entry in list_of_orderitems:
        product, created = Product.objects.get_or_create(vendor_id=entry.ASIN,
                                                         defaults={'title': entry.Title})

        if created:
            print("Product created: {} : {}".format(product.vendor_id, product.title))

        orderitem, created = OrderItem.objects.get_or_create(
            order=order,
            marketplace_orderitem_id=entry.OrderItemId,
            defaults={
                'product': product,
                'shipping_price': int(entry.ShippingPrice.Amount * 100),
                'quantity': int(entry.QuantityOrdered),
                'sku': entry.SellerSKU,
                'quantity_shipped': int(entry.QuantityShipped),
                'price': int(entry.ItemPrice.Amount * 100)
            })

        if created:
            log.info('orderitem: {} created'.format(orderitem.marketplace_orderitem_id))
        else:
            log.info('orderitem: {} already in the database'.format(
                orderitem.marketplace_orderitem_id))


def import_all_orderitems(marketplace_name):
    marketplace = Marketplace.objects.filter(name=marketplace_name)
    orders = Order.objects.filter(marketplace=marketplace)
    print("We got {} orders".format(len(orders)))
    for order in orders:
        import_orderitems(order.marketplace_order_id)
        create_invoice_for_order(order)


def import_orderitems_of_today(marketplace_name):
    marketplace = Marketplace.objects.filter(name=marketplace_name)
    start = date.today() - timedelta(days=1)
    start = start.strftime('%Y-%m-%dT00:00:00Z')
    end = datetime.now() - timedelta(minutes=90)
    end = end.strftime('%Y-%m-%dT%H:%M:%SZ')
    print("Import OrderItems from {} till {} for {}".format(
        start, end, marketplace_name))

    list_of_orders = get_list_of_orders(marketplace_name, start, end)
    import_list_of_orders(list_of_orders)

    orders_of_today = Order.objects.filter(marketplace=marketplace, insert_time__range=(start, end))
    print("We got {} orders today".format(len(orders_of_today)))

    for order in orders_of_today:
        import_orderitems(order.marketplace_order_id)
        create_invoice_for_order(order)
