from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.permissions import IsAuthenticated

from .models import Purchase
from .serializers import PurchaseSerializer


class PurchaseView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.queryset = Purchase.objects.all()
        self.serializer_class = PurchaseSerializer

    # @api_view(['GET'])
    # @authentication_classes([TokenAuthentication])
    # @permission_classes([IsAuthenticated])
    def get(self, request):

        return Response(self.serializer_class(self.queryset, many=True).data)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            purchase = serializer.save()

            return Response(self.serializer_class(purchase).data)

        return Response({'error': serializer.is_valid(raise_exception=True)})