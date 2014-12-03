# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_auto_20141202_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoice_id',
            field=models.CharField(blank=True, null=True, max_length=15),
            preserve_default=True,
        ),
    ]
