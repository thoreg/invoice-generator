from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country_code = models.CharField(max_length=2)


class Marketplace(models.Model):
    name = models.CharField(max_length=20)
    vendor_id = models.CharField(max_length=14)


class Order(models.Model):
    purchase_time = models.DateTimeField()
    insert_time = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    marketplace_order_id = models.CharField(max_length=25)
    email = models.EmailField()
    marketplace = models.ForeignKey(Marketplace)
    address = models.ForeignKey(Address)


class Invoice(models.Model):
    order = models.ForeignKey(Order)
    creation_time = models.DateTimeField(auto_now_add=True)

