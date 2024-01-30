from django.shortcuts import render
import requests
from .templates.home.LostForm import LostForm
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
    my_form = LostForm()
    if request.method == "POST":
        my_form = LostForm(request.POST)
        
        if my_form.is_valid():
            print(my_form.cleaned_data["local"])
            print(my_form.cleaned_data["item"])
            print(my_form.cleaned_data["description"])
            print(my_form.cleaned_data["contact"])

            return render(request, "home/index.html", {"lost_form": LostForm()})
            
    return render(request, "home/index.html", {"lost_form": my_form})