from django.conf.urls import patterns, include, url
from django.contrib import admin


print("kukuk")

urlpatterns = patterns(
    '',

    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    url(r'^addi/', include(admin.site.urls)),

    #(r'^sale/api/', include('sale.urls.api')),
    url(r'^sale/', include('m13.sale.urls.ui')),

    url(r'^$', 'm13.views.index', name='index')
)
