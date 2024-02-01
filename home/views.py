from django.views.decorators.csrf import csrf_exempt
from .templates.home.Form import Form
from django.shortcuts import render
import requests

def my_request():
    url = "https://us1.locationiq.com/v1/search"

    data = {
        'key': 'pk.9bac73b8821d501d511a29413e757052',
        'q': 'Viamão, RS, Brazil',
        'format': 'json'
    }

    response = requests.get(url, params = data)
    print(response.json())

@csrf_exempt
def home(request):
    my_form = Form(request.POST, auto_id=False)

    if request.method == "POST":
        
        if my_form.is_valid():
            user_loc = my_form.cleaned_data["location"]
            user_item = my_form.cleaned_data["item"]
            user_item_desc = my_form.cleaned_data["description"]
            print(user_loc, user_item, user_item_desc)

            return render(request, "home/index.html", {"lost_form": Form()})
    return render(request, "home/index.html", {"lost_form": my_form})