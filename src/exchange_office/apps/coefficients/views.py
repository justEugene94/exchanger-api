from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Coefficient, CommerceValue
from .serializers import CoefficientSerializer, CommerceValueSerializer


class CommerceValueViewSet(viewsets.ReadOnlyModelViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.queryset = CommerceValue.objects.all()
        self.serializer_class = CommerceValueSerializer

    def get_queryset(self):
        return CommerceValue.objects.all()


class CoefficientViewSet(viewsets.ModelViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.permission_classes = (IsAuthenticated,)

        self.queryset = Coefficient.objects.all()
        self.serializer_class = CoefficientSerializer