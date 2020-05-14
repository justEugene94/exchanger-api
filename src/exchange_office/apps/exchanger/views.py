import json
from urllib.request import urlopen

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request):
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

    json_url = urlopen(url)

    data = json.loads(json_url.read())

    return Response(data)