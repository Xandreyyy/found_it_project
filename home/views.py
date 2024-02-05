from django.views.decorators.csrf import csrf_exempt
from .templates.home.Form import Form
from django.shortcuts import render, redirect
import requests
from .models import LostItem
from django.utils import timezone as tz

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
            circle_radius = request.POST.get("lost_mapRadius")
            coords = get_coords(user_loc)
            # print(f"Radio: {circle_radius}")
            print(coords)
            #id_item, lost_loc, lost_latitude, lost_longetude, lost_item, item_desc, circle_radio, lost_date, lost_fk, item_status
            lost_item = LostItem(lost_loc = user_loc, lost_latitude = coords["lat"], lost_longetude = coords["lon"], lost_item = user_item, item_desc = user_item_desc, circle_radio = None, lost_date = tz.now(), lost_fk = request.user)
            lost_item.save()

            return render(request, "home/index.html", {"lost_form": Form()})
        
        elif not request.user.is_authenticated:
            return redirect("account:signin")

    return render(request, "home/index.html", {"lost_form": my_form})