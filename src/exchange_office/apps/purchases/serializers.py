from rest_framework import serializers

from .models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):

    value = serializers.IntegerField(required=True)

    customer = serializers.CharField(required=True)

    currency = serializers.CharField(required=True)

    exchange_currency = serializers.CharField(required=True)

    def create(self, validated_data):
        super().create(**validated_data)

        return Purchase.objects.create(**validated_data)


    class Meta:
        model = Purchase
        fields = ('id', 'customer', 'currency', 'exchange_currency', 'value')