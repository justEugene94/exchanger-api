from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import CurrencySerializer
from .models import Currency


class CurrencyView(viewsets.ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.queryset = Currency.objects.all()
        self.serializer_class = CurrencySerializer

    def list(self, request):

        serializer = CurrencySerializer(self.queryset, many = True)

        return Response(serializer.data)
