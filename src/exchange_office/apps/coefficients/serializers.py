from rest_framework import serializers

from .models import Coefficient


class CoefficientSerializer(serializers.ModelSerializer):

    amount = serializers.IntegerField(required=True)

    percent = serializers.FloatField(required=True, max_value=0.99, min_value=0)

    commerce_value = serializers.CharField(required=True)

    def create(self, validated_data):

        super().create(**validated_data)

        return Coefficient.objects.create(**validated_data)

    def update(self, instance, validated_data):

        super().update(instance, **validated_data)

        instance.amount = validated_data('amount', instance.amount)
        instance.percent = validated_data('percent', instance.percent)
        instance.commerce_value = validated_data('commerce_value', instance.commerce_value)

        return instance


    class Meta:
        model = Coefficient
        fields = ('id', 'amount', 'percent', 'commerce_value')