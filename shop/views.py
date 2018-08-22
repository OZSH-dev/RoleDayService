from django.shortcuts import render
from shop.models import Item


def index(request):
    items_to_sell = Item.objects.all()
    return render(request, "shop_page/shop.html", {"items": items_to_sell})

