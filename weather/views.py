# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    appid = 'b6907d289e10d714a6e88b30761fae22'
    url = 'https://api.openweathermap.org/data/2.5/' \
          'weather?q={}&appid=' + appid

    city = 'London'
    res = requests.get(url.format(city))
    print(res.text)


    return render(request, 'weather/index.html')