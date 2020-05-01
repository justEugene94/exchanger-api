from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Purchase
from .serializers import PurchaseSerializer


class PurchaseView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.queryset = Purchase.objects.all()
        self.serializer_class = PurchaseSerializer

    def get(self, request):

        return Response(self.serializer_class(self.queryset, many=True).data)

    def post(self, request):
        pass