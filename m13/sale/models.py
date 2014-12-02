from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country_code = models.CharField(max_length=2)


class Marketplace(models.Model):
    name = models.CharField(max_length=20)
    vendor_id = models.CharField(max_length=14)


class Order(models.Model):
    purchase_time = models.DateTimeField()
    insert_time = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    marketplace_order_id = models.CharField(max_length=25, unique=True)
    email = models.EmailField()
    marketplace = models.ForeignKey(Marketplace)
    address = models.ForeignKey(Address)


class Invoice(models.Model):
    order = models.ForeignKey(Order)
    creation_time = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    vendor_id = models.CharField(max_length="12")
    title = models.CharField(max_length=144)


class OrderItem(models.Model):
    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order)
    marketplace_orderitem_id = models.CharField(max_length=15, unique=True)
    shipping_price = models.IntegerField()
    quantity = models.IntegerField()
    sku = models.CharField(max_length=15)
    quantity_shipped = models.IntegerField()
    price = models.IntegerField()
