from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from intershop.settings import GOODS_PER_PAGE

from .models import Goods, Order, User, GoodsInOrder


def index(request):
    goods_list = Goods.objects.all()
    paginator = Paginator(goods_list, GOODS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'index': True
    }
    return render(request, 'goods/index.html', context)


def busket(request):
    customer = get_object_or_404(User, username=request.user.username)
    current_order, created = Order.objects.get_or_create(customer=customer, is_done=False)
    goods_in_busket_list = current_order.goods_in_order.all()
    goods_in_busket_count = current_order.goods_in_order.count()
    paginator = Paginator(goods_in_busket_list, GOODS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'count': goods_in_busket_count,
        'index': True,
        'order': current_order.id
    }
    return render(request, 'goods/busket.html', context)


@login_required
def order_apply(request, order_id):
    current_order = get_object_or_404(Order, id=order_id)
    current_order.is_done = True
    current_order.save()
    goods_in_busket_list = current_order.goods_in_order.all()
    goods_in_busket_count = current_order.goods_in_order.count()
    paginator = Paginator(goods_in_busket_list, GOODS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'count': goods_in_busket_count,
        'index': True,
        'order': order_id
    }
    return render(request, 'goods/apply.html', context)


@login_required
def goods_add_to_busket(request, goods_id):
    goods = get_object_or_404(Goods, id=goods_id)
    order, created = Order.objects.get_or_create(is_done=False, customer=request.user)
    if not GoodsInOrder.objects.filter(order=order, goods=goods).exists():
        GoodsInOrder.objects.create(order=order, goods=goods)
    else:
        goodsinorder_object = GoodsInOrder.objects.get(order=order, goods=goods)
        goodsinorder_object.quantity += 1
        goodsinorder_object.save()
    return redirect('goods:index')

@login_required
def goods_delete_from_busket(request, goods_id):
    goods = get_object_or_404(GoodsInOrder, id=goods_id)
    goods.delete()
    return redirect('goods:busket')