# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0005_auto_20141203_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(blank=True, db_index=True, max_length=16, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='issue_time',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='invoice',
            name='number',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
