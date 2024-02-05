from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateAccount
from home.models import LostItem
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def create_account(request):
    form = CreateAccount(request.POST)
    context = {"create_acc_form": form}

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request = request, template_name= "account/register.html", context= context)

def login_account(request):
    if request.method == "POST":
        user_username = request.POST.get("username")
        user_password = request.POST.get("password")

        user_login = authenticate(request = request, username = user_username, password = user_password)

        if user_login is not None:
            login(request, user_login)
            return redirect("home") 

    return render(request = request, template_name= "account/login.html")

@login_required(login_url="account:signin")
def user_account(request):
    user = request.user.pk
    user_items = get_object_or_404(LostItem, user)
    context = {"user_items": user_items}

    return render(request = request, template_name = "account/account.html", context = context)

def logout_account(request):
    logout(request)
    return redirect("home") 