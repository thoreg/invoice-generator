# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('marketplace_orderitem_id', models.CharField(max_length=15)),
                ('shipping_price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('sku', models.CharField(max_length=15)),
                ('quantity_shipped', models.IntegerField()),
                ('price', models.IntegerField()),
                ('order', models.ForeignKey(to='sale.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('vendor_id', models.CharField(max_length='12')),
                ('title', models.CharField(max_length=144)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(to='sale.Product'),
            preserve_default=True,
        ),
    ]
