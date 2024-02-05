from django.urls import path
from .views import create_account, login_account, user_account, logout_account

app_name = 'account'
urlpatterns = [
    path("", user_account, name = "account"),
    path("signup/", create_account, name = "signup"),
    path("signin/", login_account, name = "signin"),
    path("logout/", logout_account, name = "logout")
]