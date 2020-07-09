import requests
from django.conf import settings

from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from currencies.models import Currency
from purchases.models import Purchase
from coefficients.models import Coefficient


@api_view(['GET'])
def index(request):

    try:
        bank_api_response = requests.get(settings.BANK_API_RESPONSE).json()
    except Exception:
        return Response('Ошибка банка', status=status.HTTP_404_NOT_FOUND)

    for course in bank_api_response:

        if not course.get('ccy') == 'BTC':
            currency = Currency.objects.get(name=course.get('ccy'))

            sale_purchases = Purchase.objects.get_sum(currency, 'sale')
            buy_purchases = Purchase.objects.get_sum(currency, 'buy')

            coefficient_for_sale = Coefficient.objects.get_by_sum_of_purchase_amount(sale_purchases, 'sale')
            coefficient_for_buy = Coefficient.objects.get_by_sum_of_purchase_amount(buy_purchases, 'buy')

            if coefficient_for_sale:
                course['sale'] = str(round(float(course.get('sale')) * coefficient_for_sale, 5))

            if coefficient_for_buy:
                course['buy'] = str(round(float(course.get('buy')) * coefficient_for_buy, 5))

    return Response(bank_api_response)
