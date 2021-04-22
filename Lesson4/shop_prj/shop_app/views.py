from django.http import HttpResponse
from django.shortcuts import render
from .models import GoodItem


def index(request):
    all_goods = GoodItem.objects.all()
    goods_str = ', '.join(str(good) for good in all_goods)
    context = {
        'page_header': 'Все товары',
        'goods': all_goods,
    }
    return render(request, template_name='goods_list.html', context=context)
