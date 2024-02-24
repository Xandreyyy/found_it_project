from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, EmailField, PasswordInput

class CreateAccount(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "last_name", "email", "password1", "password2"]
        widgets = {
            "username": CharField(widget=CharField(attrs={"class": "field"})),
        }