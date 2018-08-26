from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from user.models import RoleUser
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def get_user_reg_page(request):
    username = request.GET["login"]
    password = request.GET["password"]
    RoleUser.objects.create_user(
        username,
        username,
        password
    )
    return JsonResponse({"login": username, "passwd": password})


def auth(request):
    user_login = request.POST["login"]
    password = request.POST["password"]
    next_page = request.GET.get("next", "/")
    try:
        parsed_username = RoleUser.objects.get(username=user_login).username
    except RoleUser.DoesNotExist:
        return redirect("/login?bad_cred=1")

    user = authenticate(request, username=parsed_username, password=password)
    if user is not None:
        login(request, user)
        return redirect(next_page)
    return redirect("/login?bad_cred=1")


def log_out(request):
    if "next" in request.GET and request.GET["next"].startswith("/"):
        next_page = request.GET["next"]
    else:
        next_page = "/"
    logout(request)
    return redirect(next_page)


def log_in(request):
    if request.user.is_authenticated:
        return redirect("/")
    content_dict = {"next": "/", "bad_cred": False, "need_auth": False}
    if "next" in request.GET and request.GET["next"] != request.path:
        content_dict["next"] = request.GET["next"]

    if "bad_cred" in request.GET and request.GET["bad_cred"] == "1":
        content_dict["bad_cred"] = True

    if "need_auth" in request.GET and request.GET["need_auth"] == "1":
        content_dict["need_auth"] = True
    return render(request, "user/authorization.html", content_dict)