# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('m13.sale.views.ui',
                       url(r'^invoice/(?P<order_id>.+)$', 'invoice', name="invoice"),
                       url(r'^$', 'index', name="sale_index"))
