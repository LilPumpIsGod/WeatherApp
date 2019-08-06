# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.


def index(request):
    appid = 'd61c2e6bc4540358004cd3601f8b4b78'
    url = 'https://api.openweathermap.org/data/2.5/' \
          'weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        print(res)
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather/index.html', context)
