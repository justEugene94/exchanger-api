from rest_framework import serializers

from .models import Coefficient, CommerceValue


class CommerceValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommerceValue
        fields = ('id', 'name',)


class CoefficientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coefficient
        fields = ('id', 'amount', 'percent', 'commerce_value')
