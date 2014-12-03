from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^addi/', include(admin.site.urls)),

    #(r'^sale/api/', include('sale.urls.api')),
    url(r'^sale/', include('sale.urls.ui')),
)
