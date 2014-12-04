# -*- coding: utf-8 -*-
from django.views.decorators.csrf import ensure_csrf_cookie

from m13.sale.services.orderitem import import_orderitems_of_today


import json

from django.http import HttpResponse


@ensure_csrf_cookie
def do_import_orderitems_of_today(request):
    data = {}

    try:
        import_orderitems_of_today('amazon_de')
        data['message'] = 'Import erfolgreich'
    except:
        data['message'] = 'Import fehlgeschlagen'

    return HttpResponse(json.dumps(data), content_type="application/json")
