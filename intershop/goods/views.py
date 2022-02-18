from django.http import HttpResponse
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
    current_order = Order.objects.filter(customer=customer, is_done=False)[0]
    goods_in_busket_list = GoodsInOrder.objects.filter(order=current_order)
    paginator = Paginator(goods_in_busket_list, GOODS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'index': True
    }
    return render(request, 'goods/busket.html', context)

