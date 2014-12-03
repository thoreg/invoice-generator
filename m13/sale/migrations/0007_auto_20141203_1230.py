# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0006_auto_20141203_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='order',
            field=models.OneToOneField(to='sale.Order'),
            preserve_default=True,
        ),
    ]
