from .models import newsdata
from .models import City
import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import requests
import json
from .forms import CityForm

# Create your views here.


def newsroom(request):
    news = newsdata.objects.all()
    date = datetime.datetime.now()
    return render(request, 'newsroom/newsroom.html', {'News': news, 'insert_date': date})


def emp(request):
    return render(request, 'newsroom/emp.html')


def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1db82256d966f336340c879abe02792f'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'newsroom/weather.html', context)
