# -*- coding: utf-8 -*-

from django.conf.urls import include, patterns, url
from rest_framework import routers

from m13.sale.viewsets.order import OrderViewSet

router = routers.DefaultRouter()

router.register(r'orders', OrderViewSet)


urlpatterns = patterns('m13.sale.views.api',

                       url(r'^import_orderitems_of_today/$',
                           'do_import_orderitems_of_today',
                           name="do_import_orderitems_of_today"),

                       (r'^', include(router.urls)))
