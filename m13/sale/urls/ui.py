# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('sale.views',
                       url(r'^invoice/(?P<order_id>.+)$', 'invoice', name="invoice"),
                       url(r'^$', 'index', name="sale_index"))
