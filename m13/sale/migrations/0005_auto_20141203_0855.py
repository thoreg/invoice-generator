# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0004_order_invoice_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceNumber',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('last_number', models.IntegerField()),
                ('marketplace_suffix', models.CharField(max_length=1)),
                ('marketplace', models.ForeignKey(to='sale.Marketplace')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='invoicenumber',
            unique_together=set([('marketplace', 'marketplace_suffix', 'year')]),
        ),
        migrations.RemoveField(
            model_name='order',
            name='invoice_id',
        ),
    ]
