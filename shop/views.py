from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from shop.models import Item
from bank.models import Transaction
from user.models import RoleUser


def get_already_bought_item_ids_set(user):
    return frozenset(x.item.id for x in Transaction.objects.filter(caller=user, item__single_buy=True))


@login_required
def index(request):
    user_single_items = get_already_bought_item_ids_set(request.user)
    items_to_sell = Item.objects.filter(~Q(id__in=user_single_items) | ~Q(transaction__state__lt=2))
    return render(request, "shop_page/shop.html", {"items": items_to_sell})


@login_required
def buy(request):
    user = request.user
    item_id = request.POST.get("item_id")
    item = Item.objects.get(id=item_id)
    user_single_items = get_already_bought_item_ids_set(request.user)
    if item.price <= user.money and item.amount > 0 and item.id not in user_single_items:
        RoleUser.objects.filter(id=user.id).update(money=user.money-item.price)
        Item.objects.filter(id=item_id).update(amount=item.amount - 1)
        Transaction.objects.create(
            caller=request.user,
            item=item,
        )
    else:
        return JsonResponse({"state": 0, "current_money": user.money})
    return JsonResponse({"state": 1, "current_money": user.money-item.price})


@login_required
def cart(request):
    return render(request, "shop_page/cart.html", {
        "items": [x for x in Transaction.objects.filter(caller=request.user, state__lt=2).all()]
    })


