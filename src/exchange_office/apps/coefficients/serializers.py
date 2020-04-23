from rest_framework import serializers

from .models import Coefficient

class CoefficientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coefficient
        fields = ('id', 'amount', 'percent', 'commerce_value')