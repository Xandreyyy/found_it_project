from django.shortcuts import render
import requests
from .templates.home.Form import Form
from django.views.decorators.csrf import csrf_exempt

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
            print(my_form.cleaned_data["location"])
            print(my_form.cleaned_data["item"])
            print(my_form.cleaned_data["description"])
            print(my_form.cleaned_data["contact"])

            return render(request, "home/index.html", {"lost_form": Form()})
            
    return render(request, "home/index.html", {"lost_form": my_form})