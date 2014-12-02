# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_auto_20141202_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='marketplace_order_id',
            field=models.CharField(unique=True, max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='marketplace_orderitem_id',
            field=models.CharField(unique=True, max_length=15),
            preserve_default=True,
        ),
    ]
