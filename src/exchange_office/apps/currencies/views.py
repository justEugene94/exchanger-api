from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import CurrencySerializer

from .models import Currency

class CurrencyView(viewsets.ViewSet):

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def list(self, request):
        queryset = Currency.objects.all()

        serializer = CurrencySerializer(queryset, many = True)

        return Response(serializer.data)
