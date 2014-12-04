# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('m13.sale.views.api',
                       url(r'^import_orderitems_of_today/$',
                           'do_import_orderitems_of_today',
                           name="do_import_orderitems_of_today"),)
