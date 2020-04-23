from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Coefficient
from .serializers import CoefficientSerializer


class CoefficientView(viewsets.ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.permission_classes = (IsAuthenticated,)

        self.queryset = Coefficient.objects.all()
        self.serializer_class = CoefficientSerializer

    def list(self, request):

        serializer = CoefficientSerializer(self.queryset, many = True)

        return Response(serializer.data)