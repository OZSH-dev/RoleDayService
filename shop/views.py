from django.shortcuts import render
from shop.models import Item
from bank.models import Transaction
from user.models import RoleUser
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def index(request):
    items_to_sell = Item.objects.all()
    return render(request, "shop_page/shop.html", {"items": items_to_sell})


@login_required
def buy(request):
    user = request.user
    item_id = request.POST.get("item_id")
    item = Item.objects.get(id=item_id)
    if item.price <= user.money and item.amount > 0:
        RoleUser.objects.filter(id=user.id).update(money=user.money-item.price)
        Item.objects.filter(id=item_id).update(amount=item.amount - 1)
        Transaction.objects.create(
            caller=request.user,
            item=item,
        )
    return JsonResponse({"current_money": user.money-item.price})


@login_required
def cart(request):
    return render(request, "shop_page/cart.html", {
        "items": [x.item for x in Transaction.objects.filter(caller=request.user).all()]
    })