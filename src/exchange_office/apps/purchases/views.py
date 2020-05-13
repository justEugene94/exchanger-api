from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from .models import Purchase
from .serializers import PurchaseSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get(request):

    return Response(PurchaseSerializer(Purchase.objects.all(), many=True).data)


@api_view(['POST'])
def post(request):

    serializer = PurchaseSerializer(data=request.data)

    if serializer.is_valid():
        purchase = serializer.save()

        return Response(PurchaseSerializer(purchase).data)

    return Response({'error': serializer.is_valid(raise_exception=True)})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show(request, pk):
    
    return Response(PurchaseSerializer(Purchase.objects.get(id=pk)).data)