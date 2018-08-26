from django.shortcuts import render, redirect
from bank.models import Transaction
from shop.models import Item
from user.models import RoleUser
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse, HttpResponseBadRequest


@staff_member_required(login_url="/login")
def transactions(request):
    return render(
        request,
        "transactions/transactions_list.html",
        {
            "transactions": reversed(Transaction.objects.all())
        }
    )


@staff_member_required(login_url="/login")
def add_money(request):
    return render(
        request,
        "shop_page/money_adder.html",
        {"users": RoleUser.objects.all()}
    )


@staff_member_required(login_url="/login")
def money_adder(request):
    team_id = int(request.POST["team"])
    money_sum = request.POST["sum"]
    result_money = RoleUser.objects.get(id=team_id).money + max(0, int(money_sum))
    RoleUser.objects.filter(id=team_id).update(money=result_money)
    return redirect("/transactions/add_money")


@staff_member_required(login_url="/login")
def modify_transaction_state(request):  # id & state -> ok
    transaction_id = request.POST.get("id")
    accept = request.POST.get("state")

    if accept and transaction_id:
        transaction_expression = Transaction.objects.filter(id=int(transaction_id))
        if accept == "1":
            transaction_expression.update(state=1)
            return JsonResponse({"state": 1})
        else:
            # revert transaction: bring item & money back
            transaction = transaction_expression.get()
            user_expression = RoleUser.objects.filter(id=transaction.caller.id)
            item_expression = Item.objects.filter(id=transaction.item.id)

            user = user_expression.get()
            item = item_expression.get()

            user_expression.update(money=user.money + transaction.item.price)
            item_expression.update(amount=item.amount + 1)
            transaction_expression.update(state=2)
            return JsonResponse({"state": 2})

    return HttpResponseBadRequest("Expected id & state params!")

