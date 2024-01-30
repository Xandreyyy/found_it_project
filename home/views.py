from django.shortcuts import render
import requests

url = "https://us1.locationiq.com/v1/search"

data = {
    'key': 'pk.9bac73b8821d501d511a29413e757052',
    'q': 'Viamão, RS, Brazil',
    'format': 'json'
}

response = requests.get(url, params = data)
print(response.json())

def home(request):
    return render(request, "home/index.html")