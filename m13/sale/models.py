from decimal import Decimal
from django.db import models
from datetime import datetime


class Address(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country_code = models.CharField(max_length=2)

    def __str__(self):
        return "{} {}".format(self.postal_code, self.name)


class Marketplace(models.Model):
    name = models.CharField(max_length=20)
    vendor_id = models.CharField(max_length=14)

    def __str__(self):
        return self.name


class Order(models.Model):
    purchase_time = models.DateTimeField()
    insert_time = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    marketplace_order_id = models.CharField(max_length=25, unique=True)
    email = models.EmailField()
    marketplace = models.ForeignKey(Marketplace)
    address = models.ForeignKey(Address)

    def __str__(self):
        return self.marketplace_order_id

    def get_total_sum(self):
        sum = 0
        for orderitem in self.orderitem_set.all():
            sum += orderitem.price
            sum += orderitem.shipping_price

        return sum / 100

    def get_total_sum_as_string(self):
        return str(Decimal('{0:.2f}'.format(self.get_total_sum())))

    def get_invoice_number(self):
        try:
            invoice_number = Invoice.objects.get(order=self).invoice_number
        except Invoice.DoesNotExist:
            invoice_number = "Noch nicht vorhanden"

        return invoice_number


class InvoiceNumber(models.Model):
    marketplace = models.ForeignKey(Marketplace)
    year = models.IntegerField()
    last_number = models.IntegerField()
    marketplace_suffix = models.CharField(max_length=1)

    class Meta:
        unique_together = ('marketplace', 'marketplace_suffix', 'year')

    @classmethod
    def generateNext(cls, marketplace, date):
        try:
            invoice_number = cls.objects.get(marketplace=marketplace, year=date.year,
                                             marketplace_suffix='')
        except cls.DoesNotExist:
            invoice_number = cls(marketplace=marketplace, year=date.year,
                                 marketplace_suffix='', last_number=0)
        invoice_number.last_number += 1
        invoice_number.save()

        return invoice_number.last_number


class Invoice(models.Model):
    order = models.OneToOneField(Order)
    creation_time = models.DateTimeField(auto_now_add=True)
    issue_time = models.DateTimeField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    invoice_number = models.CharField(max_length=16, null=True, blank=True, db_index=True)

    def __str__(self):
        return self.invoice_number

    def save(self, *args, **kwargs):
        if not self.issue_time:
            self.issue_time = datetime.now()

        if not self.number:
            self.year = self.issue_time.year
            self.number = InvoiceNumber.generateNext(self.order.marketplace, self.issue_time)
            self.invoice_number = self.full_number

        return super(Invoice, self).save(*args, **kwargs)

    @property
    def full_number(self):
        if self.invoice_number:
            return self.invoice_number
        return "%s-%s-%07d" % (self.year, self.order.marketplace_id, self.number)


class Product(models.Model):
    vendor_id = models.CharField(max_length="12")
    title = models.CharField(max_length=144)

    def __str__(self):
        self.title


class OrderItem(models.Model):
    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order)
    marketplace_orderitem_id = models.CharField(max_length=15, unique=True)
    shipping_price = models.IntegerField()
    quantity = models.IntegerField()
    sku = models.CharField(max_length=15)
    quantity_shipped = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.marketplace_orderitem_id

    def get_netto_price_as_string(self):
        return str(Decimal('{0:.2f}'.format(self.price / 119)))

    def get_brutto_price_as_string(self):
        return str(Decimal('{0:.2f}'.format(self.price / 100)))

    def get_shipping_price_as_string(self):
        return str(Decimal('{0:.2f}'.format(self.shipping_price / 100)))

    def get_single_orderitem_price_as_string(self):
        return str(Decimal('{0:.2f}'.format(self.price / 100 / self.quantity)))
