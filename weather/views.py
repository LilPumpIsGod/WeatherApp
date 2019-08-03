# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    appid = 'd61c2e6bc4540358004cd3601f8b4b78'
    url = 'https://api.openweathermap.org/data/2.5/' \
          'weather?q={}&units=metric&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }

    context = {'info': city_info}

    return render(request, 'weather/index.html', context)