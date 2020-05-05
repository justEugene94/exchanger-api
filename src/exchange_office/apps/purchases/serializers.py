from rest_framework import serializers

from .models import Purchase, Customer
from currencies.models import Currency


class CustomerSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(required=True, max_length=20)
    last_name = serializers.CharField(required=True, max_length=20)
    phone_number = serializers.CharField(required=True, max_length=20)


    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'phone_number')


class PurchaseSerializer(serializers.ModelSerializer):

    value = serializers.IntegerField(required=True)
    customer = CustomerSerializer(required=True)
    currency = serializers.CharField(required=True)
    exchange_currency = serializers.CharField(required=True)

    def create(self, validated_data):

        if 'customer' in validated_data:
            customer = validated_data['customer']

            customer_model = Customer.objects.filter(phone_number=customer['phone_number']).first()

            if not customer_model:
                customer_model = Customer.objects.create(**customer)

            validated_data['customer'] = customer_model
            validated_data['currency'] = Currency.objects.filter(name=validated_data['currency']).first()
            validated_data['exchange_currency'] = Currency.objects.filter(name=validated_data['exchange_currency']).first()

            return Purchase.objects.create(**validated_data)

    class Meta:
        model = Purchase
        fields = ('id', 'customer', 'currency', 'exchange_currency', 'value')