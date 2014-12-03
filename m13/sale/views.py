# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render_to_response
from django.template import RequestContext

from m13.sale.models import Order, OrderItem


@login_required
@ensure_csrf_cookie
def index(request):
    context = RequestContext(request)
    context['orders'] = Order.objects.all().order_by('-purchase_time')
    return render_to_response('index.html', context)


@login_required
@ensure_csrf_cookie
def invoice(request, order_id):
    context = RequestContext(request)
    order = Order.objects.get(marketplace_order_id=order_id)
    context['order'] = order
    context['orderitems'] = OrderItem.objects.filter(order=order)
    return render_to_response('invoice.html', context)
