from django.views.decorators.csrf import csrf_exempt
from .templates.home.Form import Form
from django.shortcuts import render, redirect
import requests
from .models import LostItem
from django.utils import timezone as tz
from django.http import JsonResponse

def forward_geocoding(query):
    url = "https://us1.locationiq.com/v1/search"

    data = {
        'key': 'pk.9bac73b8821d501d511a29413e757052',
        'q': query,
        'format': 'json'
    }

    response = requests.get(url, params = data)
    return response.json()

def get_coords(location):
    data = forward_geocoding(location)[0]
    lat = float(data["lat"])
    lon = float(data["lon"])
    return {"lat": lat, "lon": lon}

@csrf_exempt
def home(request):
    my_form = Form(request.POST, auto_id=False)

    if request.method == "POST":
            
        if my_form.is_valid() and request.user.is_authenticated:
            user_loc = my_form.cleaned_data["location"]
            user_item = my_form.cleaned_data["item"]
            user_item_desc = my_form.cleaned_data["description"]
            # circle_radius = request.POST.get("lost_mapRadius")
            coords = get_coords(user_loc)

            lost_item = LostItem(loc = user_loc,
                                 latitude = coords["lat"],
                                 longetude = coords["lon"],
                                 item = user_item,
                                 description = user_item_desc,
                                 circle_radio = None,
                                 user_lost = request.user,
                                 date = tz.now()
                                ) 
            lost_item.save()

            return render(request, "home/index.html", {"lost_form": Form()})
        
        elif not request.user.is_authenticated:
            return redirect("account:signin")

    return render(request, "home/index.html", {"lost_form": my_form})